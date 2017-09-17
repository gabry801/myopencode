#!/bin/bash
#set -x
if [ $(id -u) -eq 0 ]; then
    username="ansibleitamdevops"
    pubkey="ansibleitamdevops.pub"

    egrep "^$username" /etc/passwd >/dev/null
    if [ $? -eq 0 ]; then
        echo "$username exists!"
        exit 1
    else
        echo "--- Creating ansibleitamdevops user and .ssh configuration"
        useradd -m $username
        sudo -S -u $username mkdir /home/$username/.ssh; chmod 0700 /home/$username/.ssh
        cat $pubkey >> /home/$username/.ssh/authorized_keys; chown $username. /home/$username/.ssh/authorized_keys; chmod 0600 /home/$username/.ssh/authorized_keys
        echo "--- Configure sudo for ansibleitamdevops"
        echo "$username ALL=(ALL)       NOPASSWD: ALL" >>  /etc/sudoers
        echo "--- All done..now you can run Ansible plays on this server"
    fi
else
    echo "Only root may add a user to the system"
fi
exit
