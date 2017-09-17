import os
import re
import subprocess
import uuid
import sys
import time

#from invoke import run, task
#from invoke.cli import parse
#from invoke.exceptions import Exit, Failure
#from invoke.loader import FilesystemLoader

# TODO move zabbix from os.system to Invoke


# Defining variables read from conf file 'duply_plx_bkp_config.py'
CONFIG_VARS = ('default_exclude_content', 'SOURCE', 'BKP_TTL', 'xdays',
               'historical_data_path', 'SOURCE')

# Global fixed variables and standard deployed paths/file names

zabbix_monitoring = 1
duply_exclude_file_name = 'exclude'
duply_conf_file_name = 'conf'
duply_profile_root_path = '/etc/duply'


def read_config(path):
    cf = {};
    execfile(path, cf, cf)
    for v in CONFIG_VARS:
        globals()[v] = cf[v]

def deleteContent(File_name):
    with open(File_name, "w"):
        pass

def generate_exclude(duply_conf_file, duply_exclude_file):
    # Define variables
    # xdays = line_retry_delay
    deleteContent(duply_exclude_file)
    #cf = {};
    #execfile(duply_conf_file, cf, cf)
    #globals()['SOURCE'] = cf['SOURCE']
    #print 'ciao %s' % (SOURCE)

    #filebasedir = SOURCE + '/' + historical_data_path
    filebasedir = '/' + historical_data_path


    now = time.time()

    dir_list = next(os.walk(filebasedir))[1]
    #if dir_list['tmp']: dir_list.remove('tmp') TODO

    print (dir_list)

    for subfolder in dir_list:
        print "Subfolder %s" % subfolder
        full_path = filebasedir + "/" + subfolder + "/"
        timestr = time.strftime("%Y%m%d-%H%M%S")
        print timestr
        print full_path

        # process all files older than xdays
        print "\nProcessing all files older than " + str(xdays) + " days"
        print "==========================" + "=" * len(str(xdays)) + "====="
        for root, dirs, files in os.walk(full_path):
            for name in files:
                filename = os.path.join(root, name)
                regexp = re.compile(r'/2[0-9]{3}/0[1-9]|1[0-2]/')
                if regexp.search(filename):
                    if os.path.isfile(filename) and os.stat(filename).st_mtime < now - (
                        xdays * 86400) and not os.path.islink(filename):
                        # print(filename)
                        print "%s %s %s" % (filename, datetime.datetime.fromtimestamp(os.stat(filename).st_mtime),
                                        datetime.datetime.fromtimestamp(os.stat(filename).st_ctime))
                        with open(duply_exclude_file, 'a') as file:
                            file.write("- " + filename + '\n')
                            file.write(duply_exclude_file)

    with open(duply_exclude_file, 'a') as file:
        file.write(default_exclude_content + '\n')

def get_stats(log):
    log = log.splitlines()
    for item in log:
	print item
	if item[0:22] == "Last full backup date:":
		last_full_date = item[23:]
    		if zabbix_monitoring:
			os.system ("zabbix_sender -c /etc/zabbix_agentd.conf  -k backup.s3.lastfulldate -o '" + last_full_date +"'" )
	if item[0:26] == "TotalDestinationSizeChange":
		print item
		sizechange = item.split()[1]
		print sizechange
    		if zabbix_monitoring:
			os.system ("zabbix_sender -c /etc/zabbix_agentd.conf  -k backup.s3.sizechange -o " + sizechange )

    return 0


def cleanup(my_profile):
# TODO use lib
# TODO Check exit code
    os.system('duply ' + my_profile + ' purge-full')
    os.system('duply ' + my_profile + ' purge-incr --force')

def backup_files(my_profile):
# TODO Check exit code
    cmd = ('duply ' + my_profile + ' backup')
    return subprocess.check_output(cmd, shell=True)


def run(profile):

    duply_profile_path = duply_profile_root_path + '/' +  profile
    duply_conf_file = duply_profile_path + '/' + duply_conf_file_name
    duply_exclude_file = duply_profile_path + '/' + duply_exclude_file_name
    config_file = duply_profile_path + '/' + "duply_plx_bkp_config.py"

    #print config_file
    if zabbix_monitoring:
	os.system ("zabbix_sender -c /etc/zabbix_agentd.conf  -k backup.s3.running -o 1")

    read_config(config_file)
    print '1) Generate Exclude file'
    generate_exclude(duply_conf_file, duply_exclude_file)
    #print '#' * 80
    print '2) Cleaning up files older than "%s" ...' % BKP_TTL
    cleanup(profile)
    print '#' * 80
    print '3) Backing up ....'
    log_backup = backup_files(profile)
    print '#' * 80
    print '4) Getting some stats ...'
    get_stats(log_backup)

    if zabbix_monitoring:
    	os.system ("zabbix_sender -c /etc/zabbix_agentd.conf  -k backup.s3.running -o 0")

   


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Usage: python duply_plx_bkp.py duply <profile>'
    else:
        run(sys.argv[1])
