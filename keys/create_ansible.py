#!/usr/bin/python
from __future__ import print_function
import os
import subprocess

print ("--- Creating ansibleitamdevops user and .ssh configuration")
username = 'ansibleitamdevops'
os.system("useradd -d /home/%s -m %s" % (username, username))
_rc0 = subprocess.call(["sudo -S -u ansibleitamdevops mkdir /home/ansibleitamdevops/.ssh/"],shell=True)
_rc0 = subprocess.call(["sudo -S -u ansibleitamdevops touch /home/ansibleitamdevops/.ssh/authorized_keys"],shell=True)
_rc0 = subprocess.call(["chmod 0700 /home/ansibleitamdevops/.ssh/"],shell=True)
_rc0 = subprocess.call(["chmod 0600 /home/ansibleitamdevops/.ssh/authorized_keys"],shell=True)
_rc0 = subprocess.call(["cat ansibleitamdevops.pub >>  /home/ansibleitamdevops/.ssh/authorized_keys"],shell=True)
print ("--- Configure sudo for ansibleitamdevops")
_rc0 = subprocess.call(["echo \"ansibleitamdevops       ALL=(ALL)       NOPASSWD: ALL\" >>  /etc/sudoers"],shell=True)
print ("--- All done..now you can run Ansible plays on this server")

