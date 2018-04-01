#!/usr/bin/python

"""
This script is to list the various car modules available in market
Author : Ajayaghosh V L
"""

#
# Defining sub routines
#

def display_wish_car(car_manufacturer):
  
  car_show_room = {
    'Tata'    : ['Nexon', 'Bolt', 'Tiago', 'Hexa'],
    'Hundai'  : ['i10', 'i20', 'i30', 'accent', 'creta'],
    'Tayota'  : ['Qualis', 'wish', 'fortuner', 'innova'],
    'Mahinda' : ['Bolero', 'Scorpio', 'xuv', 'thar'],
  }

  print car_show_room[car_manufacturer]
  value = [asset for asset in car_show_room[car_manufacturer] if asset == 'Nexon']
  print "Best car of this car_manufacturer is : %20s" %(value)

#
# Calling defined sub routines
#

display_wish_car('Tata') 

