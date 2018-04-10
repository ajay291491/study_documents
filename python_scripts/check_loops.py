#!/usr/bin/python
#
#
#
import mysql.connector as mariadb
from datetime import datetime
import re 
#
#
#
def check_purchase_details():

    database_connect = mariadb.connect(user='remuser', password='remuser', host='rhcemaster01.svr.apac.sathsang.net', database='monthly_finance')
    query = ("SELECT * FROM Jan_2018 WHERE shop_name='fairprice'")
    databse_cursor = database_connect.cursor()
    databse_cursor.execute(query)
    counter = 0
    for entry in databse_cursor:
        while counter < 5:  
            print entry
            counter += 1
        else:
            break
check_purchase_details()
