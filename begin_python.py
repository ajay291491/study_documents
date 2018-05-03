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
# 5. Calling every odd element in the list 
# Syntax : array_name[::2]
#
# 6. Reversing an array 
# Syntax : array_name[::-1]
#
# 7. Reversing an array and list only difference of 10
# Syntax : array_name[::-10]
#
# 8.Listing an array with a difference of 10 
# Syntax : array_name[::10]
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
# * Printing all dictionary contents
# You can print all dictionary contents together by using the "items" function 
#
# Syntax  : dict_name.items()
#
# Example : Below example will print all dictionary contents together 
#
# | my_family = {
# |   "Father"   : "Ajay",
# |   "Mother"   : "Aparna",
# |   "Daughter" : "Vaiga",
# |   "Son"      : "Rishi",
# |   "Members"  : 4,
# | }
# | print my_family.items()     => This will print the output as [('Daughter', 'Vaiga'), ('Son', 'Rishi'), ('Father', 'Ajay'), ('Members', 4), ('Mother', 'Aparna')]
#
# * How to access keys from a dictionary
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
# * How to access values from a dictionery 
# You can access values from the dictionery by two methods, one is by accessing using its key second one is by using '.values()' function 
#
# Syntax : dict_name[key]
# or     : dict_names.values()
#
# Example : Below example will show us how to access values from a dictionary using .values() function
# 
# | human_values = {
# |  'anger' : 'will kill youfself',
# |  'love'  : 'will give you pleassure',
# |  'sad'   : 'slow poison',
# |  'mad'   : 'will kill others',
# | }
# | print human_values.values()
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
# | print dict_nameG
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
# * How to perform various functions with in the dictionary 
#
# del(dict_name['key']                              => This will delete a key in that array 
# dictname ['key_name'] = value                     => This will simply add a key value pair to the dictionary
# dict_name['key_name'].remove('element')           => This can be used to remove an element from a list associated with a key in the dictionary
# dict_name['key_name'].append('element')           => This will append an element to the list associated with the key in the dictionary 
# dict_name['key_name'].insert(index, 'element')    => This will insert an element in the list in certain index number within a list associated to a key in dict.
# dict_name['key_name'].sort()                      => This will sort values in that list associated with that key
# dict_name.items()                                 => This will print the complete dictionery content including all key and values 
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
# Syntax : string_name.split("delimeter")
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
# * enumerate() function
# This is an inbuilt function will help you to get the index value of an array especially when used with for loops 
# Normally you won't be needing to print or use index value of an array, but at times there will be some requirement to use index numbers 
#
# Syntax : enumerate(list_name)
# 
# Example : Below example will show how to use enumerate() function 
#
# | from datetime import datetime
# | current_time = datetime.now()
# | school_toppers = ['Gowry', 'Ammu', 'Vaiga', 'Rishi']
# | print "Result publised on %s" %(current_time)
# | for index_number, name in enumerate(school_toppers):
# |    print "%d : %s" %((index_number+1), name)
#
# * zip() function
# This function will help to access multiple list or array at the same time using a for loop
#
# Syntax  : for element_a, element_b in zip(list_a, list_a):
#           list_of _statements
#
# Example : Below example will tell us an usage about zip() function
#
# | from datetime import datetime
# | 
# | fruits = ['apple', 'orange', 'cherry', 'grapes' ]
# | likers = ['Rishi', 'Vaiga', 'Ajay', 'Appu']
# | 
# | def fruit_likers(fruit_basket, likers_list):
# |    for fruit, liker in zip(fruit_basket, likers_list):
# |        if liker != 'Ajay':
# |            print "%s like : %10s fruit" %(fruit, liker)
# |        else:
# |            print "Ajay is not residing with Family on %s" %(datetime.now())
# |            next 
# |
# | fruit_likers(fruits, likers)
#
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
# * next statement
# You can use next to skip the current execution of the loop and skip to the next one 
#
# synatax : next 
# 
# Example : Below example will shos us the usage of 'next' statement in loop
#
# | from datetime import datetime
# | 
# | fruits = ['apple', 'orange', 'cherry', 'grapes' ]
# | likers = ['Rishi', 'Vaiga', 'Ajay', 'Appu']
# | 
# | def fruit_likers(fruit_basket, likers_list):
# |    for fruit, liker in zip(fruit_basket, likers_list):
# |        if liker != 'Ajay':
# |            print "%s like : %10s fruit" %(fruit, liker)
# |       else:
# |           print "Ajay is not residing with Family on %s" %(datetime.now())
# |            next 
# | 
# | fruit_likers(fruits, likers)
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
# * for loop (with list)
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
# * for loop (with dicionary)
# You can handle each item in the dictionary using 'key' function, using this 'key' function you can call every value too in that dictionary
#
# Syntax : for key in dict_name:
#             print dict_name[key] ==> This will print value of that key associated in the dictionary 
#
# Example : Below example will show how to handle a dictionary using for loop
#
# | Ajay_family = { 'Father'   : 'Ajay',
# |                 'Mother'   : 'Aparna',
# |                 'Daughter' : 'Vaiga',
# |                 'Son'      : 'Achu', }
# |
# | def print_family_details(family_book):
# |     
# |     for role in family_book:                            => This will pick the key of the dictionary into the 'role' variable
# |        print "%-8s : %s" %(role, family_book[role])     => 'family_book[role]' will print the value of the that 'role' which is the key
# |
# | print_family_details(Ajay_family)
#
# * for .. else loop
# Similar to the 'else' condifion which we used with while loop, 'for' loop also provides else functionality
# Once all elements in the loop are completed, then else will gets executed 
#
# Syntax  : for element in array_name:
#               statements_to_execute
#           else:
#               statements_to_execute
#
# Example : Below example tell us the usage of for else
#
# | jobs = ['electronics', 'computer', 'driver', 'medical']
# | counter = 0
# | for job in jobs:
# |   print "%d : %s" %((counter+1), job)
# |   counter += 1
# | else:
# |   print "We have shown %d jobs and no more jobs left !!!" %(counter)
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 09 - Advanced way of programming in python
#-------------------------------------------------------------------------------------------------------------
# * List comprehension :  How to create dynamic list using only loop
# You can process a list using a loop and then store in an array, this can be done using one single step using below method
#
# Synatx : list_name = [ variable loop_to_iterate ]
#
# Example : Below example will show us how to consctruct an array 
#
# | second_fifty_number = [ number for number in range(50, 101) ]       => This will add 'number' which comes out of the loop into list 'second_fifty_number'
# | print second_fifty_number
#
# * List comprehension - How to create a dynamic list (using loops and conditions)
# You can also use expression modifer methods to write programs in a advanced method and which will help you to reduce the program 
#
# Synatax : list_name = [ variable_name loop_to_iterate and condition_to_test ]
# 
# Example : Below example will show us how to create a dynamic list
# 
# | odd_numbers = [ number for number in range(51) if number%2 != 0 ]   => here number will get append in the 'odd_numbers' list if the condition is true
# | print odd_numbers 
#
# * List comprehension - How to process something and store in a list
# You can process something before you store an elemnt into a list
#
# Synatx : list = [ element_variable command_to_process loops_to_process || condition_to_process ]
#
# Example : Below example will tell us how to proces and store in a list
#
# | square_of_even_numbers = [ number*2  for number in range(50) if number%2 == 0 ]
# | print square_of_even_numbers
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 10 - classes objects and methods in python
#-------------------------------------------------------------------------------------------------------------
# Python is an object oriented programming language, which means python uses a class, object and method to create programming templates which are reusable. 
# This offers a various freedom for everyone to keep reusing the classes which are defined already. Definition for class, object and method are given below. 
#
# Class   - Class is a template which is defined and which can be reused with many objects.
# Object  - Objects are the instance of the classes which are used for certain purpose using class.
# Methods - Any function which is defined inside the class is called the methods.
#
# * Class - A detailed look
# By convention class name should be starting with a 'class' keyword, then the 'class name' and the object from which class inherits. 
# That is if you look at below example it is explained better 
#
# Syntax : class class_name(object):
#
# Example : here you defined a class keyword, then class name and then the object
# | class MyClass(object):
# |   pass                    # Pass doesn't do anything it just act as a place holder instead of expression which expected by python
#
# . __init__ function 
# When we start defining a class we must always initialize a function with name '__init__' function. 
# This function is required to intialize the objects which are getting created by the class. 
# This function must always contain some arguments amongst that 'self' argument is a must and should always be there. 
# Argument 'self' refers to the name of the object itself getting created using the class. 
# If you have more arguments for those class, then it will be referred as 'self.argument_variable', this means variable getting intialized for the object
# 
# NOTE : You can think '__init__' is the function which boots up or intialize each objects the class creates.
# 
# Example : Below example will tell us how to define a class with __init__ function and self argument
#
# | class MyClass(object):
# |   def __init__(self):
# |     pass        
#
# Example : Lets define some additional argument along with the __init__ function and see how it gets processed
# 
# | class FamilyDetails(object):
# |   def __init__(self, father, mother, son, daughter):
# |     self.father   = father                                # => Here self represent the object itself and remaining arguments are passed as 'self.argument_name'
# |     self.mother   = mother
# |     self.son      = son
# |     self.daughter = daughter
# | 
# | ajay_family = FamilyDetails("Ajay", "Aparna", "Rishi", "Vaiga")
# | print ajay_family.father
# | print ajay_family.mother
# | print ajay_family.daughter
# | print ajay_family.son
# | 
# | vijayan_family = FamilyDetails("Vijayan", "Lolitha", "Rajesh", "Raji")
# | print vijayan_family.father
# | print vijayan_family.mother
# | print vijayan_family.daughter
# | print vijayan_family.son
# | 
# | anu_family = FamilyDetails("Anu", "Reshma", "Prayag", "TBD")
# | print anu_family.father
# | print anu_family.mother
# | print anu_family.son
# | print anu_family.daughter
#
# NOTE : CONTINUE LEARNING ABOUT PYTHON CLASS SCOPE DEFINTIONS FOR VARIABLE AND FUNCTIONS 
#
# * Variable scope in class 
# Based on the scope variables are devided into three types in class 

# - Global variable   : When dealing with class, you can have variable available everywere in the python program, they are called global variables.
#
# - Member variable   : Variables those available only for the members of the certain class are called member variables. 
#                     : Member variables are normally access via 'object_name.variable' outside the class.
# 
# - Instance varaible : Variables which are available to only to perticular instance of a method within a class is called as instance variable.
#
# * Methods 
# Functions which defined inside the class are called methods, we have already seen '__init__' method earlier. 
# You can also define your own methods along with the class 
#
# Example : Below example will show defining a method within a class also will help us to understand diffrent type of variables
#
# | class Check_Cars(object):
# | 
# |   city = "Delhi"                                                 # => This is a member variable, if you want access outside class, you can call it as 'tata_cars.city' with object tata_cars
# |  
# |   def __init__(self, brand, model, milage):
# |     self.brand  = brand
# |     self.model  = model
# |     self.milage = milage
# | 
# |   def milage_ranking(self):
# |     if self.milage > int(25):
# |       print  "Good Milage for %s %s with %s" %(self.brand, self.model, self.milage)
# |     else:
# |      print "Average Milage for %s %s with %s" %(self.brand, self.model, self.milage)
# | 
# |  def onroad_status(self, car_model):                           # => here 'onroad_status' is a method and and 'car_model' is an instance variable 
# |    if car_model == "Tigor":
# |       print "%-5s Onroad in 2017" %(car_model)
# |     elif car_model == "H5X":
# |       print "%-5s Onroad in 2019" %(car_model)
# |    elif car_model == "Hexa":
# |       print "%-5s Onroad in 2016" %(car_model)
# |    else:
# |      print "car_model Model do not found"
# | 
# | tata_cars = Check_Cars("Tata", "Tigor",  "25")
# | tata_cars.milage_ranking()
# |  
# | tata_models = {
# |     "Sedan"  : "Tigor",
# |     "SUV"    : "H5X",
# |     "MPV"    : "Hexa",
# | } 
# |  
# | print "You are finding the details for tata cars in %s" %(tata_cars.city)   # => member variable picked ouside the class 
# | for car_type in tata_models.keys():
# |    tata_cars.onroad_status(tata_models[car_type])
# |  
#
# Note : In the above example you have defined object as 'tata_cars' and there are two methods you can find inside the class which are 'milage_ranking' and 'onroad_status'
#      : Here model, brand and milage are the member variable available for all methods 
#      : Here car_model is an instance variable only with the method 'onroad_status'
# 
# * Class inheritance
# Classes can inherit from another class and this process is called class inheritance.
# If we take a real life example, we know cars, trucks and bikes are all vehicles, so when we say in programatic way we cam define all these three are inherited from vehicle class
# Similary each sub class sedan, suv and hatchback has super class as cars and also it can inherit few attributes from vehicles
# But at the same time any sub classes within cars class cannot inherit from Bikes class. 
# That means if we have classes with simiar attributes, then we can inherit those attributes from super class and this model is supported by few object oriented programming languages.
#
#                                |------> Sedan  
#  	       |--------> Cars---|------> Suv
#              |                 |------> Hatchback 
#              |
#              |                 |----> Mini Truck 
# Vehicles -- >  -------> Trucks-|----> Lorry 
#              |                 |----> Oil Tanker
#              |
#              |                 |----> Sicycle
#              |--------> Bikes--|----> Scooter
#                                |----> Sports Bike
#
# In similar way python also supports class inheritance, it can inherit from single super class and it also supports multiple inheritances.
#
# There are two types of classes will involves as part of the inheritance 
#
# . Super Class - This class is going to be the 'parent class' or can be called as an 'ancistor class' from which another class will get inherited. 
#                 That means attributes of super class can be used in other classes.
# . sub class   - This is going to be the class which will get inherited from it's super class.
#
# Syntax : class Super_Class_Name(object):		=> Here we are defining Super Class just as similar as any other class we learned so far
#		pass
#
#          class Sub_Class_Name(Super_class_Name):	=> Here we are defining sub class and instead object we are giving the 'super class name' as the object, so it can inherit its values
#		Process_something
#
# Example : Below example will show us about a basic class inheritance and using the methods of the super class 
#
# |
# | class Family_Name(object):                                                          # => This is the super class here 
# |   def __init__(self, names, family_name, grand_pa_name):
# |    self.names         = names
# |    self.family_name   = family_name
# |    self.grand_pa_name = grand_pa_name 
# |
# |  def return_full_name(self):
# |    for name in self.names:
# |      if name != self.family_name:
# |        print "Full name for %10s : %s, %s" %(name, name, self.family_name) 
# |
# | class Family_Members(Family_Name):                                                  # => This is the sub class getting inherited from super class 'Family_Name'
# |    def print_family_message(self):
# |        print "This is originated from  : %s" %(self.family_name)
# |
# |    def check_grand_father(self):
# |        print "Also the grand father is : %s \n" %(self.grand_pa_name)
# |
# | def print_family_details(family_members, family_name, grand_father_name):
# |    generation_names = Family_Members(family_members, family_name, grand_father_name)    # => Here object instance is created with the sub class 'Family_Members'
# |    generation_names.return_full_name(                                                   # => But we are using the method defined in the super class 'Family_Name')
# |    generation_names.print_family_message()                                              # => Here we are calling the methods which defined in the sub class, but variables referened via super class
# |    generation_names.check_grand_father()
# | 
# | first_gen_members  = ['Vijayan', "Lolitha", "Raji", "Rajesh"]
# | second_gen_memebrs = ['Ajay', 'Aparna', 'Vaiga', 'Rishi']
# | 
# | print_family_details(first_gen_members, 'Vijayan', 'Surendran')
# | print_family_details(second_gen_memebrs, 'Ajay', 'Vijayan')
# |
#
# * Overriding the __init__ method of super class 
# In the previous example we have seen the sub class is actually inheriting the '__init__' attribute from the super class. 
# Sometime this will be an advanatage but sometime it will be a limitation based on the requirements. 
# To overcome that we can have an '__init__' method on the sub class it self 
#
# Example : Below example will show us how to use seperate __init__ method for the sub class 
#
# |
# | class IndiaCars(object):
# |    def __init__(self, brand):                  # => Here super class 'IndiaCars' has its own __init__ method
# |        self.brand = brand
# |    def display_car_maker(self):
# |        print "Car make is %s" %(self.brand)
# |
# | class CarModel(IndiaCars):              
# |    def __init__(self, model):                   # => Here sub class 'CarModel' which inherits from 'IndiaCars' has also its own __init__ method
# |        self.model = model
# |    def display_car_model(self):
# |        print "Your car model is %s" %(self.model)
# |
# | leading_car_maker = IndiaCars('Tata')           # => Here both methods are assigned different objects since they hold different __init__ function 
# | leading_car_model = CarModel('hexa')
# | leading_car_maker.display_car_maker()           # => Calling the object method as needed.
# | leading_car_model.display_car_model()
# |
#
# * Overriding Super class methods
# Similar to inheriting the methods and attributes from the super class, sub class also can override the same methods which is there in the Super class.
# This can be useful in situation where you want to follow a set of methods from the superclass but not all and few you want to keep its own version in subclass.
#
# Example : In below example we are going to override one of the method from the superclass 
#
# | 
# | class School_Details(object):
# |    def __init__(self, transport, class_room):
# |       self.transport  = transport
# |       self.class_room = class_room 
# |    def kids_transportation(self):                                               # => This method is defined with name 'kids_transportation' in superclass
# |        print "This Kid will be coming to school in : %s" %(self.transport)
# |    def class_room_details(self):
# |        print "This kid is studying at class : %s" %(self.class_room)
# | 
# | class Tution_Details(School_Details):
# |     def kids_transportation(self, transport_mode):                              # => This method is defined with name 'kids_transportation' in subclass which overrides superclass
# |        print "This kid will be coming to tution centre in : %s" %(transport_mode)
# |
# | achu = School_Details("Omni", "KG1")                                            # => Here object is referred to the superclass directly and using 'kids_transportation'
# | achu.kids_transportation()
# | achu.class_room_details()
# |
# | vaiga = Tution_Details("bus", "1G")         
# | vaiga.kids_transportation("cycle")                                              # => Here object is referred to the subclass and it uses 'kids_transportation' as defined in the subclass
# | vaiga.class_room_details()
# |
#
# * 'super' call - Using a method from superclass even though sub class has the same method defined
# In the previous example we came to know how to override a method which is defined in superclass. 
# But at times we will end up in situation even though we have a overriding method defined in sub class we still need to use the same method which is in superclass.
# To solve this problem python also a provides a fascility called as 'super' call using which you can refer to the base or superclass from the subclass or derived class 
#
# Syntax : super(subclass_name, self).method_name_from_superclass(attributes)
#
# Example : Below example will show us how to work with 'super' call method to access a overriden method from superclass
# | 
# | class School_Details(object):
# |   def __init__(self, transport, class_room):
# |      self.transport  = transport
# |     self.class_room = class_room 
# |   def kids_transportation(self):                                               # => This method is defined with name 'kids_transportation' in superclass
# |     print "This Kid will be coming to school in : %s" %(self.transport)
# |  def class_room_details(self):
# |     print "This kid is studying at class : %s" %(self.class_room)
# |
# | class Tution_Details(School_Details):
# |   def kids_transportation(self, transport_mode):                              # => This method is defined with name 'kids_transportation' in subclass which overrides superclass
# |     print "This kid will be coming to tution centre in : %s" %(transport_mode)
# |   def kids_school_transportation(self):     
# |      return super(Tution_Details, self).kids_transportation()                 # => Here we are using the method which defined in the superclass using 'super' call
# | 
# | achu = School_Details("Omni", "KG1")                                            # => Here object is referred to the superclass directly and using 'kids_transportation'
# | achu.kids_transportation()
# | achu.class_room_details()
# | 
# | vaiga = Tution_Details("bus", "1G")         
# | vaiga.kids_transportation("cycle")                                              # => Here object is referred to the subclass and it uses 'kids_transportation' as defined in the subclass
# | vaiga.class_room_details()
# | vaiga.kids_school_transportation()
# |
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 11 - File Input and output 
#-------------------------------------------------------------------------------------------------------------
# You can read and write contents to the file using file objects in python, this will help you to read from and write to a file. 
#
# * File objects 
# File objects will help us to manipulate the files for reading and writing. 
# This will also raise an IOException when there is a problem with reading or writing to a file. 
#
# Syntax  : file_object_variable = open('file_name', operation_mode)
# 
# Example : my_file = open('/etc/passwd', 'r')
#
# * Various methods in handling files in python
# There are various methods available in python while handling the files using the file objects. 
#
# . open()  : This function will help to open the file for manipulation, there are various 'operation modes' available to open a file and details given below. 
#   - r     : This will help to open a file for reading 
#   - r+    : This will help to open a file for reading and writing 
#   - w     : This will help to open a new file for writing, if its a existing file then it will overwrite that file. 
#   - w+    : This will help to write and read file, while writing existing files will be overwritten 
#   - a     : This will append a file, if you are going to work with a existing file then append is the option to go. 
#   - a+    : This will help to open a file for reading as well as for appending. 
#  
# NOTE : When you add 'b' along with the operation mode then it will help you to open binary files instead of the text files. 
#
# . close() : This will help you to close an open file, it is important to close an opened file because it will help to release memory which used to handle the file. 
#
# Example : Below example will tell you how to perform an open and close function on a file 
#
# | host_file = open('/etc/hosts', 'r')
# | host_file.close()
#
# . read()  : This function will help you to read entire file as a string and return. 
#           : If we have given size along with the read function then it read the content as a string until that index number. 
#           : If the size of the file is more than the content of the file, then its stops at the EOF. 
#           : Same case applies with the size with the negative number, then also it goes until the EOF. 
#
# Syntax : read([size]) 
#
# Example : Below example will show how perform a simple read on a file 
#
# | host_file = open('/etc/hosts', 'r')
# | print host_file.read()
# | host_file.close()
#
# Example : Below example will show how perform a read operation with size arguments
#
# | dns_file = open('/etc/resolv.conf', 'r')
# | print dns_file.read(10)
# | print dns_file.read(-5)
# | dns_file.close()
#
# . readline() : This will read the first line of the file.
#              : In case there is no size mentioned, then it will return the entire the line.
#              : If there is a size parameter mentioned, it will return the string until that index number. 
#              : If there is a size parameter mentioned which is negative or more than line, then it goes until the end of line 
#
# Example : Below example will how to read a file by line
#
# | host_file = open('/etc/hosts', 'r')
# | print host_file.readline()
# | host_file.close()
#
# Example : Below example will show how to read a file by line with size 
#
# | dns_file = open('/etc/resolv.conf', 'r')
# | print dns_file.readline(5)
# | dns_file.close()
#
# . readlines() : This function will read the file line by line and retuns each line into a list.
#               : 
# | host_file = open('/etc/hosts', 'r')
# | print host_file.readlines()
# | host_file.close()
#
# | dns_file = open('/etc/resolv.conf', 'r')
# | print dns_file.readlines(1)
# | dns_file.close()
#
# * write ()
#
#  To Continue study : https://www.geeksforgeeks.org/file-objects-python/
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 12 - Remaining Chapters 
#-------------------------------------------------------------------------------------------------------------
# * Read about importing module with alias name 
# * Study detail about the logger module - https://docs.python.org/2/howto/logging.html
# * Read about perl regular expressions 
#
#
#
#
#
#
# NOTE : Read a chapter about regular expression in Python
#
#
#
#
#
#
#
#
#
#
#
#
#
#
