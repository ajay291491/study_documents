#!/usr/in/python
#
#
#

import subprocess
import re

#
#
#

release_file  = '/etc/redhat-release'
version_check = subprocess.Popen(["uname -r"], stdout = subprocess.PIPE, shell=True)
(os_version, error) = version_check.communicate()

#
#

def get_index_numbers(file):
    
    input_file = open(file, 'r')
    for word in input_file.readlines():
        split_words = word.split()
        for (index_no, element) in enumerate(split_words):
            print "Words in the file [ %s ] with element %d : %-5s" %(file, index_no, element)
    input_file.close()

#
#
#

if re.search(r'^4\.11.+', os_version) is not None:
    get_index_numbers(release_file)
else:
    print "You are not running on Fedora Linux and current kernel version is : %s" %(os_version)

#
#
# End
