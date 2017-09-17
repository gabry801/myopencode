# Global fixed variables and standard deployed paths/file names

duply_exclude_file_name = 'exclude'
duply_conf_file_name = 'conf'
duply_profile_root_path = '/etc/duply'
duply_profile_path = duply_profile_root_path + '/' +  profile_name
duply_conf_file = duply_profile_path + '/' + duply_conf_file_name
duply_exclude_file = duply_profile_path + '/' + duply_exclude_file_name
config_file = duply_profile_path + '/' + "duply_plx_bkp_config.py"

# Data path from where generate the list of files to exclude from the backup
historical_data_path = 'data'

# leave it empty
SOURCE = ''

BKP_TTL = '90D'

#After how many days untouched / unmodified the files in the 'historical_data_path' will be considered for exclusion from backup
xdays = '90'

historical_data_path = 'data'

default_exclude_content = """+ /data/PolluxFts/Archive/DB/
- /data/PolluxFts/Archive/
- /data/PolluxFts/LineTests/
- /data/Makedonija/
+ /pollux
+ /data
- **
"""
