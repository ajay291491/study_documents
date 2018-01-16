#!/usr/bin/python
#-------------------------------------------------------------------------------------------------------------
# Chapter 01 - Basics
#-------------------------------------------------------------------------------------------------------------
# * This is how you will assign a variable
# | name = "Ajayaghosh V L"
#
# * This is how you will print the length of a variable 
# | print len(name)
#
# * This is how you will convert variable to upper case
# | print name.upper()
#
# * This is how you will convert variable to lower case
# | print name.lower()
# 
# * How to print elements of a variable using the index value, index value starts from 0
# | print name[5:]
# | print name[:5]
#
# * This is how you will add two numbers and print it 
# | num_one = 10
# | num_two = 20
# | total = (num_one + num_two)
# | print ("Sum of", num_one, "and", num_two, "is :", total)
# 
# * This is how you will make multiline comments 
# | """" here I am going to make a multi line comment
# | It can be about anything """
#
# * Single line comment 
# | # This is a single line comment
#
# * How to perform basic mathematical functions
# | number = 10
# | print "one percentage of", number, "is", (10/100)
#
# * How to convert a number to a string 
# | number = str(10)
# | print number[:1]
#
# * String concatination 
# You can use '+' sign to concatinate multiple strings together 
#
# Example : Below are we are adding few variabled and strings using concatication
#
# | name = "ajay"
# | age = "32"
# | country = "singapore"
# | print name + " is aged " + age + " and he lives in " + country
# 
# When you concatinate a number with a string, you need to convert that number into string before you concatinate 
# 
# Example : Below example shows how to concatinate a number along with string 
#
# | name = "ajay"
# | country = "singapore"
# | print name + str(32) + " aged lives in " + country
#
# * Advanced string concatination using placeholders
# Rather than using '+' sign you can use 'place holders' to declare the variables in a statement and can define all variables in the last by %(var_one, var_two, etc)
# This will pick the variable in the order you have given in the %() array.
#
# There are mainly two place holders 
# %s    - To print string
# %d    - To print digits
#
# Example : You can see an example for advnaced string concatination using %s below
#
# | fruit_one = "apple"
# | fruit_two = "orange"
# | fruit_three = "strawberry"
# | total_fruits = 3
# | print "There are %d fruits in the basket %s %s %s" %(total_fruits, fruit_one, fruit_three, fruit_two)
# | print "These %s and %s fruits can be taken to schoool, but %s can only to hospital" %(fruit_two, fruit_three, fruit_one)
#
# NOTE : Make sure the number of '%s' you have in the sting and variables with in %( ) should be same, else the compilation will fail
#
# * datetime function
# While working on scripts we will need to keep track of our time, we can use the datetime function to keep track of the time.
# See below examples to understand about various usages of datetime.now function
# 
# Example : Below example we are importing the datetime function and printing the value directly 
# 
# | from datetime import datetime
# | print datetime.now()
# 
# Example : Below example we are assiging the value of datetime.now() to current_time variable and calling printing it via advanced string concatination
# 
# | from datetime import datetime
# | current_time = datetime.now()
# | print "Current time is : %s" %(current_time)
#
# Example : Below example will show you about various other usages of timedate function to cut down each values 
#
# | from datetime import datetime
# | current_time = datetime.now()
# | print "Current time is    : %s" %(current_time)
# | print "Current year is    : %s" %(current_time.year)
# | print "Current month is   : %s" %(current_time.month)
# | print "Current date is    : %s" %(current_time.day)
# | print "Current hour is    : %s" %(current_time.hour)
# | print "current minutes is : %s" %(current_time.minute)
# | print "current second is  : %s" %(current_time.second)
# | print "current Year is %s and Month is %s" %(current_time.year, current_time.month)
# | print "current date %s-%s-%s" %(current_time.day, current_time.month, current_time.year)
# | print "current time %s:%s:%s" %(current_time.hour, current_time.minute, current_time.second)
#
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 02 - Conditionals and controll flow 
#-------------------------------------------------------------------------------------------------------------
#
# * Conditional Operators
# Conditional operators are used to compare the values between two values, based on the comparison the rsult will be either "True" or "False"
#
# ==    : equals 
# !=    : not equal to
# <=    : less than or equal to
# >=    : greater than or equal to
# <     : les than
# >     : greater than
#
# * Boolean operators 
# Boolean operators are used to compare multiple values together there are mainly three boolean operators 'and' , 'or' & 'not'
# 
# True and True    = True 
# True and False   = False
# Flase and True   = False
# False and False  = False 
# 
# True or True     = True 
# True or Flse     = True
# False or True    = True
# False or False   = False 
# 
# Not True         = False 
# Not False        = True 
#
# * if condition statement
# if is a conditional statement which excutes if the value is 'True' 
# 
# syntax : if params_one conditional_operattor params_two :
#              statemant_to_execute
# 
# Example : below example will show us the usage for if
# 
# | name = raw_input("Please enter your name : ")
# | if name == "ajay" :
# |   print "Thanks for entering your name as : %s" %(name)
#
# * if .. else conditional statement
# When you use this conditional statement, all conditions or functions which are True will get executed in if statement and false will get executed in else 
# 
# Syntax : if function(): 
#              execute the true condition
#          else: 
#              execute the false condition
#
# Example : below example will explain you about an if else condition
#
# | from datetime import datetime
# | country_name = raw_input("Please Enter your Country : ")
# | state_name   = raw_input("Please Enter your State : ")
# | current_time = datetime.now()
# | print "\nYour values are read at : %s-%s-%s %s:%s:%s \n" %(current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second)
# | if country_name == state_name: 
# |    print "You are living in a small country %s" %(country_name)
# | else:
# |     print "You are living in a big contry where your country is %s and state is %s" %(country_name, state_name)
#
# * if..elif..else conditional statement
# When you have multiple keys to match before taking a decission then you can use if..elif..else statements 
#
# Synatx : if function():
#              statements 
#          elif function():
#              statements
#          else:
#              statements
#
# Example : Below example will tell you about the usage of if..elif
#
# | def choose_your_fruit(fruit):
# |     if fruit == "apple":
# |         return "king of fruits"
# |    elif fruit == "orange":
# |        return "Tangy and prince"
# |    else:
# |        return "No match found"
# | #print choose_your_fruit('apple')
# | #print choose_your_fruit('orange')
# | user_input = raw_input("Please enter your fruit Choice : ")
# | print "You have choosen : %s - " %(user_input) + choose_your_fruit(user_input)
#      
#-------------------------------------------------------------------------------------------------------------
# Chapter 03 - inputs
#-------------------------------------------------------------------------------------------------------------
# * raw_input
# You can request an user input in a script using 'raw_input' function 
# 
# variable = raw_input("Enter your input : ")
#
# Example : Below example will show you how to take an user input
#
# | name = raw_input("Please enter your name : ")
# | print "You have entered : %s" %(name) 
#
# * .isalpha method 
# You can use '.isalpha' method to make sure any varibale input given is alphabetical then it gives the value 'True'
# If you have entered a non-alphebetical charecter then it will return the value as "False"
# 
# Synatx : variable.isalpha()
#
# Example : Below example will print the value only if the variable is alphabetical charector
#
# | name = raw_input("Please enter your name : ")
# | if name.isalpha():
# |    print "You have entereted a name : %s " %(name)
#
# Pending : Chapter 3 9/11
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 04 - Functions 
#-------------------------------------------------------------------------------------------------------------
#
# * Functions 
# Rather than writing the whole code in a single script best way is to devide each chunk of code as 'functions' which can do certian purpose. 
# When you start writing codes with functions, you will be able to re-use the same function again and again in the same code which will help you to reduce the total code. 
# This will also bringings easiness in managing the script 
#
# There are few things which are mandatory while defining the function 
# def                   - def should be mentioned when you define a function
# function_name         - name of the function 
# (list_of_inputs)      - List of inputs to the functions
# :                     - column must be there after the inputs and before the contents starts 
# """ comment """"      - Comment about the functionality 
#
# Syntax : def function_name(list_of_inputs):                               ==> This is how you will define the functions (input can be optional based on the requirement)
#            """ Here we should include the purpose of the function """     ==> This will help to idenity the purpose of the function (mandatory)
#               contents_1
#               contents_2
#
# When you call or declare a function, then you can use 'function_name' 
# ()    - You can give input to function as a list when you declare this, if there is nothing to pass you can just leave () empty to satisfy the syntax  
#
#           function_name()                         ==> This is how you can call the functions, you can even give input in the paranethesis for the function as a list
#           function_name(input_to_function)        ==> You can call function in this way also if you have a input or list of input to pass
#
# Example : Below is an example for defining function and giving a string input
#
#   | def check_availability(order): 
#   |   """ This function is to check the order availability """
#   |    if order == "burger":
#   |       print "%s is available" %(order)
#   |    elif order == "fries":
#   |       print "%s is available" %(order)
#   |    else:
#   |       print "You order not available : %s" %(order)
#   |
#   | def check_order():
#   |   """ This function will take user input as an order"""
#   |   item_name = raw_input("Please enter your item : ")
#   |   check_availability(item_name)
#   |		
#   | check_order()
#
# Example : Below example will show us the usage of calling a function with multiple parameters
#
# | def money_converter(money_amount, conversion_rate):                 => This function takes two parameter as inputs while defining
# |    """ Does the conversion """
# |    effective_rate = (money_amount * conversion_rate)
# |    print "Your effective conversion rate is %d x %d = %d" %(money_amount, conversion_rate, effective_rate)
# |
# | def collect_user_input():
# |   """ Takes user input """
# |    money_amount = int(raw_input("Please enter the amount of money you have : "))
# |    conversion_rate = int(raw_input("Please enter the conversion rate : "))
# |    money_converter(money_amount, conversion_rate)                   => Here it declare the function with two parameter taken from user input
# | 
# | collect_user_input()
#
# * Importing a module 
# In python there are amble amount of modules available which can used to perform various predefined actions
# By using pre-defined modules, you are avoiding the duplication of code and can achieve your task simply by calling the function within th module 
# Modules are called into the script by using a keyword 'import'and once modules are imported we can use functions within that modules according to their usage 
#
# Syntax : import module_name
#          module_name.function_name ()     #  => You need to use this like module_name.function_name
#
# Example : Below example shows us the square root of a 'number'
#
# | import math
# | number = 25
# | result = math.sqrt(number)
# | print "Your resuly is : %d" %(result)
#
# * Importing only a function from a module 
# Lets say rather than using 'math.sqrt' function on the above example, you want to directly use it as 'sqrt()' function. 
# To do that you can directly import that specific function from that module.
# 
# Syntax : from 'module_name' import 'function_name'
#          function_name (variable)
#
# Example : Below example will show us how to only import sqrt function from math module
#
# | from math import sqrt
# | 
# | def sqrt_of_number(input_num):
# |     """ This function finds the square root of a number """
# |     if input_num:
# |        square_root = sqrt(input_num)                              """ ==> Here we are using only sqrt() function and not calling the module """
# |        print "Square root of %d : %d" %(input_num, square_root)
# |
# | number = int(raw_input("Please Enter your number :"))
# | sqrt_of_number(number)
#
# * Importing all functions in a module 
# If you want to import all functions from a module rather than only one function then you can use below synatx to call all the functions 
#
# syntax : from module_name import *
#
# NOTE : using this method is not advisable since there will be multiple functions from various modules may have same name that can cause confusion
#        To avoid ending up in such situations it is always recomended that you will need to only use only below two method 
#        1. use 'import module'  and then use 'module_name.function_name' method 
#        2. use 'from module_name import function_name' method only to use the required function from that module 
#
#
# * How to list all functions within a module 
# To list all functions available with the module, you can use dir() function to convert all option as a list 
# 
# Example : synatx and example given below for further understanding
#
# | import math
# | function_list = dir(math)
# | print "\nList of functions available with module \'math\' are : \n\n %s" %(function_list)
#
# * Default or inbuilt functions in pythons
# There are many inbuilt functions in python which you can use without importing any additional modules
# You can get the complete details of these modules by referring to below link 
# 
# Source : https://docs.python.org/3/library/functions.html
# 
# There are few builtin functions which we need to be aware of 
#
# min ()    => This will give you the minimum values from a list , e.g : min_value = min(-10, 10, 20, -100)    : Here result will be -100
# max ()    => This will give you the maximum or biggest value in a list , e.q : max_value = max(-10, 10, 20, -100)    : Here result will be 20
# abs()     => This will give you the absolute value of a number, that is distance from zero distance = abs(-10)       : Here rsult will be 10
# type()    => This will resturn the type of the variable or data is either int, float or string, this will be very useful ehen you are writing if condition to check the type if the input
# 
#-------------------------------------------------------------------------------------------------------------
# Chapter 05 - List and various methods to handle 
#-------------------------------------------------------------------------------------------------------------
#
# * List 
# List can be used store more than one value in a variable. It can be either a string or numbers. 
# When you define a set of values with in a list you need to put then inside [ ] which separated by commas. 
# 
# Syntax : zoo = [ 'tiger', 'panda', 'monkey', 'dear']
#
# Example : Below example show us sample list 
#
# | from datetime import datetime
# | current_time = datetime.now()
# | def zoo_animals():
# |     zoo_animals = ['tiger', 'elephant', 'dear', 'monkey']
# |    print "If you go to zoo on %d th on you can see : %s" %(current_time.day, zoo_animals)
# |
# | zoo_animals()
#
# * Array or list slicing (method to access elements in an array)
# You can access elements in the array in 4 different methods
#
# 1. Call the element expicitly by the index number of that element
# Syntax : array_name[x]    => here x is the index name 
# 
# 2. Give a range, if you want to access a portion of an array then use the range method.
# Syntax : aray_name[x:y]   => Here 'x' means index value of the first element to start with and 'y' means any element before the 'y' index 
#
# 3. Calling any elements any elments before any specific index number 
# Syntax : array_name[:y]   => This will slice any elements before index y
#
# 4. Calling any elements after any specific index number 
# Syntax : array_name[x:]   => This will slice as x and any elements after that.
#
# Example : below example you will see how to access list elemnts with any index number of range 
#
# | def display_new_cars():
# |    tata = ['hexa', 'nexon', 'tigor', 'bolt']
# |    maruthi = ['swift', 'breza', 'dzire', 'waganor']
# |    hundai = ['creta', 'i10', 'i20', 'ion']
# |    new_cars = [tata, maruthi, hundai]
# |    print "These are the new cars available in the market \n => %s" %(new_cars)
# |    print "Tata cars => %s" %(new_cars[0])
# |    print "Tata and Maruthi cars : %s " %(new_cars[0:2])
# |    print "Maruthi and Hunday cars : %s" %(new_cars[1:3])
# |    print "Any car excluding Hundai : %s" %(new_cars[:2])
# |    print "Any excluding Tata %s : " %(new_cars[1:])
# |
# | display_new_cars()
#
# - You can retrieve each element from the list by giving the index number of the array elements, index number always starts from zero
#
# zoo_animals = [ 'tiger', 'elephant', 'deer', 'monkey'] 
# index numbers =>  0           1        2        3
#
# | user_input = int(raw_input("Please Enter the index number : "))
# | 
# | def display_zoo_animal(index_number):
# |    zoo_animals = ['tiger', 'elephant', 'dear', 'monkey']
# |    if index_number < 4:
# |        print  zoo_animals[index_number]
# |    else:
# |        print "out of range"
# |
# | display_zoo_animal(user_input)
#
# - You can also add or replace values by assigning values to the curresponding values 
#
# menu = ['tea', 'coffe', 'ice cream', 'juice', 'bread', 'rice']
# | print menu
# | menu = menu + ['sambar']
# | print menu
# | menu[1] = 'vodka'
# | print menu
# | menu [5] = ''
# | print menu
#
# * How find the length of list (using object len)
# You can find the length of a list using object 'len',
#
# Syntax : len(array)
#
# Example : Below example will show you how to find the length of an array
#
# | car_park = ['ford', 'tata', 'maruthi', 'hundai']
# | total_cars = len(car_park)
# | print "Total number of cars in cark park are : %d" %(total_cars)
#
# * How to append a list
# You append elements into a list by using the 'list_name.append' method 
#
# Synatax : array_name.append('element')
#
# Example : Below example will show you how to append an item to an array 
# 
# | car_park = ['ford', 'tata', 'maruthi', 'hundai']
# | car_park.append('honda')
# | car_park.append('bajaj')
# | print car_park
# 
# * Many methods in list object
#
# - How to find the index number of an elme                         => array_name.index("element")                  # Example : car_park.index[3]
# - How to replace an element in an array with index number         => array_name.insert(index_number, "element")   # Example : car_park.insert[2, "Honda"]
# - How to sort an element in an array                              => array_name.sort                              # Example : car_park.sort
# - How to remove an element from an array                          => array_name.remove(element)                   # Example : car_park.remove("Honda")
# - How to remove an element using index number                     => array_name.pop(index_number)                 # Example : car_park.pop(0)
# - How to remove an elemnt with its name                           => array_name.remove(element)                   # Example : car_park.remove('ford')
# - How to remove and element from an array using del()             => del(array_name[index_number])                # Example : del(car_park[0])
# - How to append to a list                                         => array_name('element')                        # Example : car_park('Maruti')
# - How to multiply an array and append to a list                   => array_name([array_element] * count]          # Example : car_park(['Jeep'] * 5)
#
# Example : Below example will show the usage of .index and .insert method in list object
#
# | from datetime import datetime
# | current_time = datetime.now()
# | family = ['Achu', 'vaiga', 'Aparna', 'Ajay']
# | def replace_value(current_name, nick_name):
# |     index_number = family.index(current_name)
# |     if type(index_number) == int:
# |        family.insert(index_number, nick_name)
# |        print "My sweet family : %s this was processed at date %d-%s-%d" %(family, current_time.day, current_time.month, current_time.year)
# |
# | print "Your family : %s" %(family)
# | current_name = raw_input("Please choose your family member name as shown above : ")
# | nick_name = raw_input("Please enter the nickname of %s :" %(current_name) )
# | replace_value(current_name, nick_name)
#
#
# Example : Below example will explain about various usage of list removal
#
# | grocery_items = ['lendil', 'rice', 'wheat', 'piece']
# | total_item = len(grocery_items)
# | first_removal = grocery_items.pop(0)
# | second_removal = grocery_items.remove('rice')
# | print "There are total of %d items available and %s and %s removed now" %(total_item, first_removal, second_removal)
# | print "remaining items are %s" %(grocery_items)
#
# * for loop 
# When you want to perform an action on set of action in all elements of a list then you can use for loop to achieve that task 
#
# Syntax : for variable_name in list_name:
#               Do_the_stuff
#
# Example : Below example will show the usage of for loop
#
# | family = ['Achu', 'vaiga', 'Aparna', 'Ajay']
# | for member in family:
# |    print member
#
# Example : using for loop along with sorting a number array 
#
# | serial_numbers = [10, 20, 50, 40 ,32, 56, 21, 39]
# | serial_numbers.sort()
# | for number in serial_numbers:
# |     square = number**2
# |     print "Square of %-3d => %5d" %(number, square)
# 
#
# * Using list in a function 
# When you are writing a function you can use list as an input to the function. 
# 
# Synatx : function_name(list_name)  or function_name(list_of_elements)
#
# Example : Below example will show us the usage of list in the function
#
# | def detect_manufacturer(cars):
# |     total_tata_cars = 0 
# |     total_hundai_cars = 0
# |     total_maruthi_cars = 0 
# |   for car in cars:
# |         if car == 'hexa' or car == 'nexon' or car == 'tiago':
# |            total_tata_cars = total_tata_cars + 1
# |        elif car == 'creta' or car == 'i10' or car == 'eon':
# |            total_hundai_cars = total_hundai_cars + 1
# |        elif car == 'baleno' or car == 'breza' or car == 'alto':
# |            total_maruthi_cars = total_maruthi_cars + 1
# |    return (total_tata_cars, total_hundai_cars, total_maruthi_cars)
# |
# | cars = [ 'breza', 'hexa', 'alto', 'creta', 'beleno', 'tiago', 'nexon' , 'eon']
# | print detect_manufacturer(cars)
#
# 
#-------------------------------------------------------------------------------------------------------------
# Chapter 06 - Dictionaries
#-------------------------------------------------------------------------------------------------------------
# Dictionaries are two dimensional array or list and they consist of the key value pair.
# Similar to list, rather than accessing elemnt via an index number, you can access the values with the keys in a dictionary
# Dictionaries are stored in curely braces { } and the way store is like below 
#
# Synatx : dictionary_name = {
#               'key_one'   : value_one,
#               'key_two'   : value_two,
#               'Key_three' : value_three,
#          }
#
# Syntax : dictionary_name['key_one']   => This will give the result as value_one
#
# Example : Below example will show you an usage about dictionary using for loop
#
# | family = {
# |     'Son'       : 'Achu',
# |     'Daughter'  : 'Vaiga',
# |     'Mother'    : 'Aparna',
# |     'Father'    : 'Ajay',
# |     }
# | print family['Son']
# | print family['Daughter']
# | print family['Mother']
# | print family['Father']
#
# * Adding values to dictionary 
# Similar to a list, dictionaries are also mutable, that means you can add values to the dictionry even after you have created it 
# To add a value to the existing dictionary you need to asign a key : value pair using below syntax 
# 
# Syntax : dict_name['new_key'] = value 
#
# Example : Below example will show how to add a key value pair to a dictionary
#
# | dict_name = {
# |     'Daughter'  : 'Vaiga',
# |     'Mother'    : 'Aparna',
# |     'Father'    : 'Ajay',
# |     }
# | dict_name['Son'] = "Achu"
# | print dict_name
#    
# * Delete values from dictionary
# You can delete values also from dictionary using below syntax 
#
# Syntax : del dict_name['key_name']
#
# Example : You can delete values from dictionary as below
#
# | cars = {
# |    'tata'    :   ['hexa', 'nexon'],
# |    'maruti'  :   ['brezza', 'boleno'],
# |   'hundai'  :   ['i10', 'eon'],
# | }
# |
# | print cars
# | user_input = raw_input("Enter the car company you want to remove : ")    
# | del(cars[user_input])
# | print "You have only these cars left in showroom : %s" %(cars)
#
# * How to pull only keys from a dictionary
# You can pull only keys from a dictionary and it can be used further to achieve various tasks, you can pull key as below 
#
# Synatx : dict_name.keys()
#
# Example : Print elements in a dictionary and delete or modify what you do not need
#
# | human_needs = {
# |     'charector'     : 'This defines whom you are',
# |     'wish'          : 'This defines what you want to be',
# |     'jelous'        : 'This will make you devil',
# |     'kindness'      : ['philanthrophy', 'marathon', 'help'],
# |     }
# | 
# | for charector_type in human_needs.keys():
# |     if charector_type == 'jelous':
# |         del(human_needs[charector_type])                    """ => This will delete the key and value"""
# |     if charector_type == 'kindness':
# |         human_needs[charector_type].remove('marathon')      """ => This will remove only an element in list associated with that key """
# |         
# | print human_needs
#
# * How to perform various functions with in the dictionary 
#
# del(dict_name['key']                              => This will delete a key in that array 
# dictname ['key_name'] = value                     => This will simply add a key value pair to the dictionary
# dict_name['key_name'].remove('element')           => This can be used to remove an element from a list associated with a key in the dictionary
# dict_name['key_name'].append('element')           => This will append an element to the list associated with the key in the dictionary 
# dict_name['key_name'].insert(index, 'element')    => This will insert an element in the list in certain index number within a list associated to a key in dict.
# dict_name['key_name'].sort()                      => This will sort values in that list associated with that key
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 07 - Few builtin function which is useful in day to day 
#-------------------------------------------------------------------------------------------------------------
# In this chapter we will see the usage of few of builtin functions which can be used for day to day scripting
# 
# * How to get all possible usage of a module 
# To get all possible usage of a module, you can call that function with in a dir() function 
# 
# Syntax : dir(function_name)
#
# Example : below examples will tell us the usage of the various functions 
#
# | import math
# | import datetime
# | print dir(range)        # This will print all options inside range()
# | print dir(math)         # This will print all options inside math()
# | print dir(datetime)     # This will print all options inside datetime()
#
# * datetime()
# This function will help us to print various datetime formats and details 
# 
# Method  : import datetime                 => This is how you can import the datetime module completely
# or      : from datetime import datetime   => This is how you can import only datetime() function from datetime module
# synatx  : current_time = datetime.now()   => This will store complete datetime value to variable current_time
#         : current_time.day                => This will print the current date
#         : current_time.hour               => Thus will print the details of the current hour 
#         : current_time.month              => This will print the details of current month
#         : current_time.year               => This will print the details of current year
# details : dir(datetime)
#
# * range ()
# This  is a python inbuilt function which can be used to get a range of numbers as a list
# 
# Syntax : rang(to_what_number)
#        : range(from_number, to_number)
#
# Example : Below example will help you to understand the usage of the range() function 
#
# | def display_even_numbers(from_number, to_number):
# |   numbers = range(from_number, to_number)
# |   even_numbers = []
# |   odd_numbers  = []
# |   for number in numbers:
# |     if (number % 2) == 0:
# |      even_numbers.append(number)
# |    else :
# |      odd_numbers.append(number)
# |  print "Odd number in the list is : %s"  %(odd_numbers)
# |  print "Even number in the list is : %s" %(even_numbers)
# | 
# | display_even_numbers(20, 40)
#
#
# * split() function
# We can use split function to split a string using any delimeter within the string and produce a list
# Delimeter can be " " "," /  \  :  . or any other of these kind of symbols   
# 
# Syntax : string_name.split("delimeter"
#
# Example : Below example will show us how to split a string and store it in an array
# 
# | def split_a_sentence(sentence):
# |   lists = sentence.split(" ")
# |   count = 0
# |   for word in lists:
# |     count = count + 1
# |     print "%d : %s" %(count, word)
# |
# | split_a_sentence("My name is Ajay")
#
#
# * join() function
# This function can be used to join or concatinate a list in to a string using any  given delimeter 
# Delimeter can be " " "," /  \  :  . or any other of these kind of symbols   
#
# Syntax : "delimeter".join("list")
#
# Example : Below example will show us the usage about join function 
#
# | def join_a_list(lists):
# |  joined_word = ' : '.join(lists)
# |   return joined_word
# | 
# | word_1 = "My name is"
# | word_2 = "Ajay"
# | lists=[word_1, word_2]
# | 
# | print join_a_list(lists)
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 08 - Loops 
#-------------------------------------------------------------------------------------------------------------
# * While loop 
# While loop will continue to execute the loop until the given condition is true 
#
# Synatx : while condition_to_check:
#            steps_to_execute
#
# Example : Below example will show how to use a while loop 
#
# | def check_your_while_loop(max_range):
# |   counter = 0
# |   if max_range > 5:
# |     while counter < max_range:
# |       print counter
# |       counter += 1 
# |   else:
# |     print "Range is too short"
# | 
# | max_number = raw_input("Please enter your number : ")    
# | check_your_while_loop(int(max_number))
#        
# * How to increase counter in a loop 
# There are two methods you can use for increasing the counter after intializing your counter
#
# method 1 : counter = counter + 1
# method 2 : counter += 1
#
# * break statement
# break statement will help you to exit out of the loop. 
#
# Syntax : break 
#
# Example : Below example will show the usage of break
#
# | def fruits_basket(fruits):
# |   for fruit in fruits:
# |    if fruit == 'apple':
# |      print "I cannot eat this fruit %s, tray returned" %(fruit)
# |      break
# |    else:
# |      print fruit
# |
# | fruits = []
# | input_fruit = raw_input("Please Enter your fruit name : ")
# | while input_fruit != 'end':
# |  fruits.append(input_fruit)
# |  input_fruit = raw_input("Please Enter your fruit name : ")
# | 
# | fruits_basket(fruits)
#
# * While else loop ()
# One thing which is peculiar about python is while else, not all languuages provides that feature. 
# While else will be working like this 
# - while loop will get excuted until the condition is true 
# - if the condition comes false then while will skip and else will get executed
# - at any point in time if you are using break in the while loop, then else condition won't be processed
#
# Syntax : while condition_to_check:
#               steps_tor_execute
#           else:
#               steps_to_execute 
#
# Example : Below example will tell us how to use a while else loop
#
# | import random
# | def display_random_number(user_input):
# |   counter = 0 
# |   while counter < 10:
# |     number = random.randint(0, int(user_input))
# |     print number
# |     counter += 1
# |     if number > 9:
# |       print "Detected random number greater than 9 and is : %s" %(number)
# |      break
# |  else:
# |    print "You have exceed your counter limit of 9"
# | 
# | user_input = raw_input("Please enter your number choice : ")
# | display_random_number(user_input)
#
# * for loop
# for loop can be used to perform action on a list of items, this can process the list of statements given according to the number of elements given inthe list 
# 
# Syntax : for variable_name in list_name
#               statement_to_execute
#
# Example : Below example will show us an usage of for loop using a list created by range
#
# | for number in range(0, 15):
# |  if number < 10:
# |    print number,                    => This comma will cut down the new line 
# |  else:
# |    print "You have exceed limit"
# |    break
#
# Example : Below example will tell us an usage of using for loop from a list 
#
# | def test_your_array():
# |   family = ['aparna', 'ajay', 'vaiga', 'rishi']
# |   for member in family:
# |     if member is "ajay":
# |       print "%10s : is currently overseas" %(member)
# |     else:
# |       print "%5s : is current in India" %(member)
# | 
# | test_your_array()
#   
#
#

