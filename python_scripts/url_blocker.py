#!/usr/bin/python
#
# Desc : Script to disable website in study times
#

#
# Declaring Modules needed for the functions
#

from   datetime  import datetime
from   shutil    import copyfile
import platform
import re
import os
import sys

#
# Declaring global variables needed for function
# 

time_stamp   = datetime.now()
current_time = str(time_stamp.time()).split(':')[0]
host_file    = '/etc/hosts'
hostname     = platform.node()
tool_name    = 'url_manager'
url_to_block = {
  'manorama'     : 'manoramaonline.com',
  'mathrubhumi'  : 'mathrubhumi.com',
  'cnn'          : 'cnn.com',
  'bbc'          : 'bbc.com',
  'ndtv'         : 'ndtv.com',
  'economictime' : 'economictimes.com',
}

#
# Defining subroutines
#

def update_logfile(comment):
  logfile_fh = open('/var/log/messages', 'a')
  message    = "%s : %s : %s : %s \n" %(time_stamp, hostname, tool_name, comment)
  logfile_fh.write(message)
  logfile_fh.close()

#
# Declaring Class  
#

class Manage_Web_Url(object):

  def __init__(self):
    pass

  def take_backup(self):
    backup_file = '/etc/hosts.bkp.urlblocker'
    copyfile(host_file, backup_file)
    

  def disable_url(self, url_name):
    url_counter = 0
    disable_url_string = '127.0.0.1 www.' + url_name
    if os.path.exists(host_file):
      read_file = open(host_file, 'a+')
      for line in read_file.readlines():
        if re.search(r'^\d.+url_name$', line) is not None:
          url_counter += 1
      if url_counter == 0 :
        read_file.write(disable_url_string)
        read_file.write("\n")
      read_file.close()

  def enable_url(self):
    master_file = '/etc/hosts.master'
    if os.path.exists(master_file):
      copyfile(master_file, host_file)  
          
#
# Definig functions
#

def url_manager(state):

  if state == 'disable':
    for site in url_to_block.keys():
      site_url = url_to_block[site]
      site = Manage_Web_Url()
      site.disable_url(site_url)
      update_logfile("Disbaled access to news website %s now" %(site))
  elif state == 'enable':
    url_state = Manage_Web_Url()
    url_state.enable_url()
    update_logfile("Enabled access to news websites now")
  else:
    update_logfile("Invlid action selected")


#
# Processing script
# 

url_manager(sys.argv[1])

#
# End of script
# 

  








