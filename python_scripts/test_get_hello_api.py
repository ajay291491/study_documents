#!/usr/bin/python
#
# Script to check the working status of hellp.api
#

from pprint import pprint
import requests 

#
main_url = 'http://rhceclient01.svr.apac.sathsang.net:8080/api/'
sub_url  = 'hello-view/'
#
def get_api_content(bae_api, api_key):
    
    full_url = bae_api + api_key
    connect = requests.get(full_url)
    pprint (connect.json())

get_api_content(main_url, sub_url)

