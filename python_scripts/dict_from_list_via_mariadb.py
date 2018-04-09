#!/usr/bin/python
#

import mysql.connector as mariadb

#

family_memebrs = ['ajay', 'aparna', 'vaiga', 'rishi']
car_details = { }

mariadb_connection = mariadb.connect(user='anu', password='anu275', host='rhcemaster01.svr.apac.sathsang.net', database='indian_cars')
cur = mariadb_connection.cursor()
query = ("SELECT car_name FROM suv where car_manufacturer='Tata'")
cur.execute(query)

for (user, car) in zip(family_memebrs, cur):
    car_details[user] = car

print car_details.items()    
