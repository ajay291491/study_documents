#!/usr/bin/python
#
# DESC : Script to manage monthly_finance table in MariaDB
#

#
# Importing required modules 
#

import mysql.connector as mariadb
from datetime import datetime

#
# Declaring variables 
#

current_time = datetime.now()

#
# Defining subroutines 
#

def get_car_models_available(manufacturer):
  mariadb_connection = mariadb.connect(user='user_name', password='pass_word', host='rhcemaster01.svr.apac.sathsang.net', database='indian_cars')
  cur = mariadb_connection.cursor()
  query = ("SELECT car_name FROM suv where car_manufacturer='Tata'")
  cur.execute(query)
  for cars in cur:
    print cars
  mariadb_connection.close()

#
# Calling subroutine
#

get_car_models_available('Tata')

#
#
# End
