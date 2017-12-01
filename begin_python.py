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
"""" here I am going to make a multi line comment
It can be about anything """
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
# * Advanced string concatination using placeholder '%s'
# Rather than using '+' sign you can use '%s' to declare the variables in a statement and can define all variables in the last by %(var_one, var_two, etc)
# This will pick the variable in the order you have given in the %() array.
#
# Example : You can see an example for advnaced string concatination using %s below
#
# | fruit_one = "apple"
# | fruit_two = "orange"
# | fruit_three = "strawberry"
# | print "There are three fruits in the basket %s %s %s" %(fruit_one, fruit_three, fruit_two)
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
#
