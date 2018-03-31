#!/usr/bin/python
from datetime import datetime
current_time = datetime.now()
def display_date(date):
  if date:
    print date 
    
display_date(current_time.day)    
