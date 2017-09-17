# AWS Backup role for Ansible

Installs and configures the AWS CLI and configure it for conveniently interacting with AWS services such as S3.

## Requirements

Tested on EL 5/7.

## Role Variables

The default variables are as follows:
 No default variables are used in this playbook

## Example Playbook main file.


    - hosts: 'servers'
      roles:
        - role: 'aws-backup'
      

# License

This playbook is provided 'as-is' under the conditions of the BSD license. No fitness for purpose is guaranteed or implied.

# How to run the playbook:
  - create a var file (under var/) with the name country name (eg: Macedonia : macedonia.yml) with the following variable:values
        aws_access_key_id: 'AKIAJYPENEJMLOHLJ6HA'
        aws_secret_access_key: '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'
        bucket_name: "mace-pollux-test" 
        aws_region: "eu-west-1" 
        duply_profile: "polluxfts" 
        dir_on_bucket: "{{ ansible_hostname }}
  - 'cd' into 'pollux_RUN' direcotory
  - insert into 'hosts' file all the needed info, eg: '10.95.2.197 country=macedonia'
  - run the playbook: ansible-playbook -i hosts aws-backup.yml
