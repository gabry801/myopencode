# AWS CLI role for Ansible

Installs and configures the AWS CLI on EL 5/6/7.


## Requirements

Tested on EL 5/7 Server.

## Role Variables

The default variables are as follows:

    aws_output_format: 'json'
    aws_region: 'ap-southeast-2'
    aws_access_key_id: 'YOUR_ACCESS_KEY_ID'
    aws_secret_access_key: 'YOUR_SECRET_ACCESS_KEY'

## Example Playbook

    - hosts: 'servers'
      roles:
        - role: 'aws-cli'
          aws_output_format: 'json'
          aws_region: 'ap-southeast-2'
          aws_access_key_id: 'SUPER_SECRET_ACCESS_KEY_ID'   # Don't version this or put it on pastebin
          aws_secret_access_key: 'SUPER_SECRET_ACCESS_KEY'  # Ditto

# License

This playbook is provided 'as-is' under the conditions of the BSD license. No fitness for purpose is guaranteed or implied.
