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
# NOTE : Make sure the number of '%s' you have in the sting and vriables with in %( ) should be same, else the compilation will fail
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
#
#
#


