#!/usr/bin/python
#
#

from subprocess import call as command 
from math import sqrt 
import re
import os
import sys

#
#

"""
def get_range_of_numbers(lower_limit, upper_limit):
    return range(lower_limit, upper_limit)


def find_sqrt_for_range(lower_limit, upper_limit):
    square_root_sum = 0
    for number in range(lower_limit, upper_limit):
        sqrt_result = sqrt(number)
        print sqrt_result
        square_root_sum = (square_root_sum + sqrt_result)
    print "Sum of all the square root is : %s" %(square_root_sum)
"""

def split_your_file(file_name):
    my_file = open(file_name, 'r')
    for line in my_file.readlines():
        if re.search(r'^#', line) is None:
            for word in line.split():
                if re.search(r'^/dev', word) is not None:
                    print (command(['blkid', word]))
#
#

"""
min_limit = int(raw_input("Please Enter your minimum range : "))
max_limit = int(raw_input("You have entered minimum limit as %s, Now enter your Maximum limit :" %(min_limit)))
"""

#
#

"""
print get_range_of_numbers(min_limit, max_limit)
find_sqrt_for_range(min_limit, max_limit)
"""

split_your_file("/etc/fstab")
