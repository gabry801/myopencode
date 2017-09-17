# ansible-role-pam-pwquality

RHEL/CentOS - PAM module to perform password quality checking

## Requirements

None

## Role Variables

All default variables are listed below

    pam_pwquality_dcredit: 1
    pam_pwquality_difok: 5
    pam_pwquality_gecoscheck: 0
    pam_pwquality_lcredit: 1
    pam_pwquality_maxrepeat: 0
    pam_pwquality_maxclassrepeat: 0
    pam_pwquality_minclass: 0
    pam_pwquality_minlen: 9
    pam_pwquality_ocredit: 1
    pam_pwquality_ucredit: 1

Additional variable not defined by default

    pam_pwquality_dictpath: /path/to/cracklib/dictionaries

## Dependencies

None
 
## Example Playbook

    - hosts: servers
      roles:
        - role: linuxhq.pam-pwquality
          pam_pwquality_dcredit: -1
          pam_pwquality_difok: 8
          pam_pwquality_gecoscheck: 1
          pam_pwquality_lcredit: -1
          pam_pwquality_maxrepeat: 4
          pam_pwquality_maxclassrepeat: 4
          pam_pwquality_minclass: 4
          pam_pwquality_minlen: 15
          pam_pwquality_ocredit: -1
          pam_pwquality_ucredit: -1
    
## License
## Author Information
