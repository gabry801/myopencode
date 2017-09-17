# Data path from where generate the list of files to exclude from the backup
historical_data_path = 'data'

# leave it empty
SOURCE = ''

BKP_TTL = '90D'

#After how many days untouched / unmodified the files in the 'historical_data_path' will be considered for exclusion from backup
xdays = '90'

default_exclude_content = """+ /data/PolluxFts/Archive/DB/
- /data/PolluxFts/Archive/
- /data/PolluxFts/LineTests/
- /data/Makedonija/
+ /pollux
+ /data
- **
"""
