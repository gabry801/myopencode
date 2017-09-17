#!/bin/bash
#set -x
#array=('s1=(10.7.134.32 chiniy01 TrustCI01!)' 's2=(10.7.134.33 caimma-90 ch@ng3mE)' 's3=(10.7.134.34 caimma-90 ch@ng3mE)' 's4=(10.7.134.35 caimma-90 ch@ng3mE)' 's5=(10.7.134.36 caimma-90 ch@ng3mE)' 's6=(10.7.134.52 caimma-90 ch@ng3mE)')
array=('s1=(10.241.65.25 agbsupport LoveTennis0503)' 's2=(10.241.65.21 root t2:hlvb!)' 's3=(10.241.65.41 root t2:hlvb!)' 's4=(10.241.65.42 root t2:hlvb!)')
for connection in "${array[@]}";do eval $connection; done
echo "${s1[@]}"
echo "${s2[@]}"
echo "${s3[@]}"
echo "${s4[@]}"
echo "${s5[@]}"
echo "${s6[@]}"
echo "sshpass -p \"${s1[2]}\" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null create_ansible.sh ansibleitamdevops.pub ${s1[1]}"@"${s1[0]}:~"
echo "sshpass -p \"${s2[2]}\" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null create_ansible.sh ansibleitamdevops.pub ${s2[1]}"@"${s2[0]}:~"
echo "sshpass -p \"${s3[2]}\" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null create_ansible.sh ansibleitamdevops.pub ${s3[1]}"@"${s3[0]}:~"
echo "sshpass -p \"${s4[2]}\" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null create_ansible.sh ansibleitamdevops.pub ${s4[1]}"@"${s4[0]}:~"
echo "sshpass -p \"${s5[2]}\" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null create_ansible.sh ansibleitamdevops.pub ${s5[1]}"@"${s5[0]}:~"
echo "sshpass -p \"${s6[2]}\" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null create_ansible.sh ansibleitamdevops.pub ${s6[1]}"@"${s6[0]}:~"
