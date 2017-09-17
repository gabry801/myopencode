#!/usr/bin/python
import pickle
#from Pickling import Pickling 
import ldap
import sys
import yaml
import pprint, pickle
import json

host = 'ldap://ldap-sen.enterprisenet.org:389'
dn = 'pscomm88@enterprisenet.org'
pw = 'Tyrion!234'
base_dn = 'OU=Accounts,dc=enterprisenet,dc=org'
yamlfile = 'default.yml'

# DEFINITION OF SECURITY GROUPS TO CYCLE
grouplist = {"devops":['itamdevops,OU=North America','Y'], "appdev":['iTAM PE Administrators','N'] }


def get_users_from_group(group,fileout,sudoacc):
    #print(group)
    filter = 'memberOf=CN=%s,OU=Groups,DC=enterprisenet,DC=org' % group
    #print(filter)
    attrs = ['sAMAccountName', 'cn', 'mail']
    con = ldap.initialize( host )

# Bind to the server
    con.simple_bind_s( dn, pw )
    res = con.search_s( base_dn, ldap.SCOPE_SUBTREE, filter, attrs )
    #print (res)

# Close the connection
    con.unbind()

    for i in res:
                lanid = str(i[1]["sAMAccountName"])
                lanid = lanid.lower()
                cn = str(i[1]["cn"])
                b = "[,]'-"
                for char in b:
                    cn = cn.replace(char,"")
                    lanid = lanid.replace(char,"")
                #print (fileout + ' ' + cn + ' ' + lanid + ' ' + sudoacc + ' ' + lanid + ' ' + '.pub"' + ' Y')
                this_active='Y'

                #uservalues = {lanid:[NAMESURNAME(cn),GRUPPO,ACTIVE(Y/N),SUDO(Y/N),KEYFILE]}
                #uservalues = {lanid:[cn,fileout,'Y',sudoacc,lanid + '.pub'] }
                if any(lanid in d for d in userlist):
                    if userlist[lanid][3] == 'Y':
                        userlist[lanid][0] = cn
                        userlist[lanid][1] = fileout
                        userlist[lanid][2] = 'Y'
                    else:
                        userlist[lanid][0] = cn
                        userlist[lanid][1] = fileout
                        userlist[lanid][2] = 'Y'
                        userlist[lanid][3] = sudoacc
                else:
                    userlist.update({lanid:[cn,fileout,'Y',sudoacc,lanid + '.pub'] })



def deleteContent(File_name):
    with open(File_name, "w"):
        pass

# START PROGRAM

# DELETE YAML FILE
deleteContent(yamlfile)

# DOWNLOAD FROM GIT JSON FILE
# !!!!

# CREATE INITIAL DICTIONARY (userlist) BASED ON JSON FILE CONTENT
with open('userlist.json', 'r') as fp:
    userlist = json.load(fp)

"""
# DEBUG ONLY: print dictionary content
for value in userlist.items():
    print ('lanid: ' + value[0] + ', cn: ' + value[1][0] + ', Group: ' + value[1][1] + ', Active: ' + value[1][2] + ', Sudo: ' + value[1][3] + ', Key: ' + value[1][4] )
"""

# RESET DICTIONARY PERMISSION FIELDS FOR ALL USERS
for value in userlist.items() :
    # Update Active value to N for all users in dictionary
    userlist[value[0]][2] = 'N'
    # Update Sudo value to N for all users in dictionary
    userlist[value[0]][3] = 'N'

# RETRIEVE ACTIVE DIRECTORY USERS FOR ALL SECURITY GROUPS
for value in grouplist.items():
    #print ('Group: ' + value[0] + ', AD: ' + value[1][0] + ', SUDO: ' + value[1][1] )
    get_users_from_group(value[1][0],value[0],value[1][1])

"""
# DEBUG ONLY: print dictionary content
for value in userlist.items():
    print ('lanid: ' + value[0] + ', cn: ' + value[1][0] + ', Group: ' + value[1][1] + ', Active: ' + value[1][2] + ', Sudo: ' + value[1][3] + ', Key: ' + value[1][4] )
"""


# GENERATE YAML FILE
with open(yamlfile, 'a') as yamlfile:
#filename  = open('default.yml',"a")
#   sys.stdout = filename
    yamlfile.write('---')
    for group in grouplist.items():
        yamlfile.write('\n'+group[0]+'_users:\n') 
        for user in userlist.items():
            if user[1][1] == group[0]:
                yamlfile.write("  " + user[0] + ':'+ " "'{name: \"'  + user[1][0] + '\"' + ',' + " " + 'lanid: \"' + user[0] + '", keyfile: "' + user[0] + '.pub"' + ', active: \"' + user[1][2] + '\", sudo: \"' + user[1][3] + '\"}\n')


# EXPORT DICTIONARY TO JSON FILE
with open('userlist.json','w') as fp:
    json.dump(userlist, fp)

# COMMIT JSON FILE AND YAML FILE TO GIT
# !!!!!

