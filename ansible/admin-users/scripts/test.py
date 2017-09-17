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
#grouplist = {"devops":['itamdevops,OU=North America','Y'], "appdev":['iTAM PE Administrators','N'] }
group = "itamdevops,OU=North America"

    #print(group)
filter = 'memberOf=CN=%s,OU=Groups,DC=enterprisenet,DC=org' % group
    #print(filter)
attrs = ['sAMAccountName', 'cn', 'mail']
con = ldap.initialize( host )

# Bind to the server
con.simple_bind_s( dn, pw )
res = con.search_s( base_dn, ldap.SCOPE_SUBTREE, filter, attrs )
print (res)

# Close the connection
con.unbind()

