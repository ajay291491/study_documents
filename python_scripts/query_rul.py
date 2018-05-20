#!/usr/bin/python
#
# Purpose : Script to query an API 
#

from pprint import pprint 
import requests 
import re 

#
# Declaring variables 
#

main_url = 'http://httpbin.org'
single_date = {'name': 'Ajay'}
couples = {'husband': 'Ajay' , 'wife': 'Aparna'}
family  = {'father': 'Ajay', 'mother': 'Aparna', 'kids': ['Vaiga', 'Rishi']}

#
# Delaring subroutines 
#

def process_post_requests(input_data):
  post_url = main_url + '/post'
  data_post = requests.post(post_url, input_data)
  status = data_post.status_code
  if status == 200:
   print "Info (post) : Content posted successfully %s" %(input_data)
  else: 
   print "Fail (post) : Unable to post data"

def process_get_requests(input_data):
  get_url = main_url + '/get'
  sub_url_raw = ""
  pair = ""
  for keys in input_data:
   if type(input_data[keys]) is list:
      for element in input_data[keys]:
        pair = pair + '&'  + keys + '=' + element  
      sub_url_raw = pair + '&'
   else:
     pair = keys + '=' + input_data[keys] 
   sub_url_raw = sub_url_raw + pair + '&'
  sub_url = re.sub(r'\&$','', sub_url_raw)
  content = requests.get(get_url + '?' + sub_url)
  status = content.status_code
  print status
  if int(status) == 200:
    print "Info (get) : Query was successful and content is below **\n"
    pprint (content.json())
  else:
    print "Fail (get) : Query was not successful"

def process_requests(input_data):
  process_post_requests(input_data)
  process_get_requests(input_data)

#
# Invoking subroutines
#

process_requests(single_date)
process_requests(couples)
process_requests(family)

