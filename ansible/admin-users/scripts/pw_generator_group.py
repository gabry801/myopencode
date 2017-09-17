#!/usr/bin/python
import random
import crypt
import sys
import smtplib
from email.mime.text import MIMEText

email =  sys.argv[1]
server = sys.argv[2]

def hash512(password):
    h = crypt.crypt(password, "$6$")
    return(h)

if __name__ == '__main__':
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = 8
    p =  "".join(random.sample(s,passlen ))
    #print ("Password is: " + p)
    #passin = getpass('Please enter clear-text password: ')
    #print("SHA512 :: " + hash512(p))
    myemail='polluxl1support@nielsen.com'

    body = "This is an auto generated email. \n \n We have created an account for your lanid on: %s with password: %s \n In case of issues contact PolluxL1Support@nielsen.com" % (server, p)
    msg = MIMEText(body)
    subj= 'Your access to %s' % server
    msg['Subject'] = subj
    msg['From'] = myemail
    msg['To'] = email
    s = smtplib.SMTP('smarthost.enterprisenet.org')
    s.sendmail(myemail, [email], msg.as_string())
    s.quit()
    print hash512(p)
