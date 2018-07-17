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
# * Types of Operator
# Python language supports the following types of operators.
# 
#    . Arithmetic Operators
#    . Comparison (Relational) Operators
#    . Assignment Operators
#    . Logical Operators
#    . Bitwise Operators
#    . Membership Operators
#    . Identity Operators
# 
# Let us have a look on all operators one by one.
#
# * Python arithamatic operator
# 
# [ Show Example ]
# Operator 		Description 								Example
# + Addition 		Adds values on either side of the operator. 				a + b = 30
# - substraction        substracts right hand operand from left hand operand                    a - b = -10
# * Multiplication 	Multiplies values on either side of the operator 			a * b = 200
# / Division 		Divides left hand operand by right hand operand 			b / a = 2
# % Modulus 		Divides left hand operand by right hand operand and returns remainder 	b % a = 0
# ** Exponent 		Performs exponential (power) calculation on operators 			a**b =10 to the power 20
# 
# These operators compare the values on either sides of them and decide the relation among them. They are also called Relational operators.
# 
# Assume variable a holds 10 and variable b holds 20, then
# 
# [ Show Example ]
# Operator 	Description 	Example
# == 	If the values of two operands are equal, then the condition becomes true. 						(a == b) is not true.
# != 	If values of two operands are not equal, then condition becomes true. 							(a != b) is true.
# <> 	If values of two operands are not equal, then condition becomes true. 							(a <> b) is true. This is similar to != operator.
# > 	If the value of left operand is greater than the value of right operand, then condition becomes true. 			(a > b) is not true.
# < 	If the value of left operand is less than the value of right operand, then condition becomes true. 			(a < b) is true.
# >= 	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. 	(a >= b) is not true.
# <= 	If the value of left operand is less than or equal to the value of right operand, then condition becomes true. 		(a <= b) is true.
# 
# 
# * Python Assignment Operators
# Assume variable a holds 10 and variable b holds 20, then
# 
# [ Show Example ]
# Operator 			Description 											Example
# = 				Assigns values from right side operands to left side operand 					c = a + b assigns value of a + b into c
# += Add AND 			It adds right operand to the left operand and assign the result to left operand 		c += a is equivalent to c = c + a
# -= Subtract AND 		It subtracts right operand from the left operand and assign the result to left operand 		c -= a is equivalent to c = c - a
# *= Multiply AND 		It multiplies right operand with the left operand and assign the result to left operand 	c *= a is equivalent to c = c * a
# /= Divide AND 		It divides left operand with the right operand and assign the result to left operand 		c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a
# %= Modulus AND 		It takes modulus using two operands and assign the result to left operand 			c %= a is equivalent to c = c % a
# **= Exponent AND 		Performs exponential (power) calculation on operators and assign value to the left operand 	c **= a is equivalent to c = c ** a
# //= Floor Division 		It performs floor division on operators and assign value to the left operand 			c //= a is equivalent to c = c // a
# 
# * Python Bitwise Operators
# Bitwise operator works on bits and performs bit by bit operation. Assume if a = 60; and b = 13; Now in binary format they will be as follows
# a = 0011 1100
# b = 0000 1101
# -----------------
# a&b = 0000 1100
# a|b = 0011 1101
# a^b = 0011 0001
# ~a  = 1100 0011
# 
# There are following Bitwise operators supported by Python language
# 
# [ Show Example ]
# Operator 			Description 	Example
# & Binary AND 			Operator copies a bit to the result if it exists in both operands 	(a & b) (means 0000 1100)
# | Binary OR 			It copies a bit if it exists in either operand. 	(a | b) = 61 (means 0011 1101)
# ^ Binary XOR 			It copies the bit if it is set in one operand but not both. 	(a ^ b) = 49 (means 0011 0001)
# ~ Binary Ones Complement 	It is unary and has the effect of 'flipping' bits. 	(~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.
# << Binary Left Shift 		The left operands value is moved left by the number of bits specified by the right operand. 	a << 2 = 240 (means 1111 0000)
# >> Binary Right Shift 	The left operands value is moved right by the number of bits specified by the right operand. 	a >> 2 = 15 (means 0000 1111)
# 
# 
# * Python Logical Operators
# There are following logical operators supported by Python language. Assume variable a holds 10 and variable b holds 20 then
# 
# [ Show Example ]
# Operator 		Description 								Example
# and Logical AND 	If both the operands are true then condition becomes true. 		(a and b) is true.
# or Logical OR 	If any of the two operands are non-zero then condition becomes true. 	(a or b) is true.
# not Logical NOT 	Used to reverse the logical state of its operand. 			Not(a and b) is false.
# 
# * Membership Operators
# Python's membership operators test for membership in a sequance, such as strings, lists, or tuples. There are two memebership operators as explained below 
# 
# [ Show Example ]
# Operator 	Description 											Example
# in 		Evaluates to true if it finds a variable in the specified sequence and false otherwise. 	x in y, here in results in a 1 if x is a member of sequence y.
# not in 	Evaluates to true if it does not finds a variable in aspecified sequence and false otherwise.	x not in y, here not in results in a 1 if x is not a member of sequence y.
# 
# * Python Identity Operators
# Identity operators compare the memory locations of two objects. There are two Identity operators explained below
# 
# [ Show Example ]
# Operator 	Description 														Example
# is 		Evaluates to true if the variables on either side of the operator point to the same object and false otherwise. 	x is y, here is results in 1 if id(x) equals id(y).
# is not 	Evaluates to false if the variables on either side of the operator point to the same object and true otherwise. 	x is not y, here is not results in 1 if id(x) is not equal to id(y).
# 
# 
# * Python Operators Precedence
# The following table lists all operators from highest precedence to lowest.
# 
# [ Show Example ]
# Sr.No. 	Operator & Description
# 1 	**			Exponentiation (raise to the power)
# 2 	~ + -			Complement, unary plus and minus (method names for the last two are +@ and -@)
# 3 	* / % //		Multiply, divide, modulo and floor division
# 4 	+ -			Addition and subtraction
# 5 	>> <<			Right and left bitwise shift
# 6 	&			Bitwise 'AND'
# 7 	^ |			Bitwise exclusive `OR' and regular `OR'
# 8 	<= < > >=		Comparison operators
# 9 	<> == !=		Equality operators
# 10 	= %= /= //= -= += *= **=Assignment operators
# 11 	is is not		Identity operators
# 12 	in not in		Membership operators
# 13 	not or and		Logical operators
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
# By using pre-defined modules, you are avoiding the duplication of code and can achieve your task simply by calling the function within the module 
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
# | print "Your result is : %d" %(result)
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
# To list all functions available within the module, you can use dir() function to convert all option as a list 
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
# min ()    => This will give you the minimum values from a list , e.g : min_value = min(-10, 10, 20, -100)            : Here result will be -100
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
# . open()  : This method will help to open the file for manipulation, there are various 'operation modes' available to open a file and details given below. 
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
# . read()  : This method will help you to read entire file as a string and return. 
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
# . readlines() : This method will read the file line by line and retuns each line into a list.
#               : 
# | host_file = open('/etc/hosts', 'r')
# | print host_file.readlines()
# | host_file.close()
#
# | dns_file = open('/etc/resolv.conf', 'r')
# | print dns_file.readlines(1)
# | dns_file.close()
#
# . write ()    : This method will help you to write content  as a string into the file. 
#               : Due to buffering you wont be able to see the content inside the file until you call the close() or flush() method. 
# 
# Example : Below example will show how to use the write method using write operation mode.
#
# | my_file = open('/tmp/testfile', 'a+')
# | print my_file.readlines()
# | my_file.write('This is a test file' "\n")
# | my_file.close()
#
# . writelines() : This method will help you write a list of string into the file. 
#
# Example : Below example will tell you how to write a file using writelines() method 
#
# | my_file = open('/tmp/testfile', 'w+')
# | my_file.writelines('This file is now tested for another method' 'This is the second string')
# | my_file.close()
#
# . tell()      : This method will tell us what is the position of the cursor from the beginning of the file 
#
# Example : Below is an example for tell method 
#
# | host_file = open('/etc/hosts', 'r')
# | print host_file.readline(7)
# | print host_file.tell()
# | host_file.close()
#
# . seek(offset, from_where) : This method will change the file's object position. 
#                            : Here 'offset' indicates the number of bytes to be moved. 
#                            : 'from_where' indicates from which position this needs to be moved. 
#
# Example : Below example will show us about the seek method 
#
# | with open('/etc/hosts', 'r') as host_file:
# |   print host_file.read(30)
# |   print host_file.seek(25)
# |   print host_file.read(30)
#
# . flush()     : Flush the internal buffer. close() automatically flushes the data but if you want to flush the data before closing the file then you can use this method.
#
# Example :  Clearing the internal buffer before closing the file
#
# | with open('/tmp/testfile', 'w+') as test_file:
# |   print test_file.write('This is a test message')
# |   test_file.flush()
# |   print test_file.read()
#
# . closed ()  : This method can be used to test whether you file is already closed or not 
#
# Example : Below example will show how to test whether the file is closed or not. 
#
# | with open('/tmp/testfile', 'r') as test_file:
# |  print test_file.read(10)
# | 
# | if not test_file.closed:                #  => Note that we did not use '()' here for testing 
# |   test_file.close()
# | else:
# |   print "test_file already close"
#
# * How to close a file object automatically (with .. as method)
# There are two methods actually used by python when you call the file objects. 
# When you call open it actually invokes the _enter_() function and when you close the file it call the __exit__() function. 
# So using the 'with ..as' method you can let python to automatically close the file rather than you invoke the close() function.
# 
# Example : Below example will show the with as method. 
#
# | with open('/etc/hosts', 'r') as host_file:
# |   print host_file.readline(10)
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 12 - Python best practices
#-------------------------------------------------------------------------------------------------------------
#
# * space and tabs
#  . Always try to use space rather than tab for intendation. 
#  . Do not mix space and tab for programming, python 3 disallows mixing both space and tab in the same program.
#
# * Intentation
#  . Use 4 spaces per indentation level. 
#  . Continuation lines should align wrapped elements either vertically using Python's implicit line joining inside parentheses, brackets and braces, or using a hanging indent.
#
# * Maximum Line Length
#  . Limit all lines to a maximum of 79 characters.
# 
# * Imports
#  . Imports should be normally on seperate lines, multiple import on the same line is not recomended. 
#  . Imports should be grouped in the following order 
#    1. standard library imports
#    2. Third party imports 
#    3. Local application or library specific imports
#  . Import only what you need with its absolute name, rather than loading all the module. 
#
# Example : Below example show the style of imports 
#
# | import sys
# | import os
# | import re 
# | from datetime import datetime
#
# * Whitespaces in Expression and statements
#  . Avoid white spaces as much as possible under paranthesis, lists, dictionry etc. 
#  . One white space after the comma should be fine 
#  . Also avoid trailing white spaces. 
#
# NOTE : For more details on python styling guide refer : https://www.python.org/dev/peps/pep-0008/
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 13 - Regular expressions
#-------------------------------------------------------------------------------------------------------------
# In Python regular expressions are used for processing text. 
# That means, for finding a pattern of text using various regular expression patterns. 
# 
# In python regular expressions are processed using the 're' module, to start with processing regular expression you will need to import this module.
# There are mainly two methods used within regular expression matching and one additional method for substituion. 
#
# - re.match()   : This will search for the string within the beginning of the string. 
# - re.search()  : This will search within the entire text and will create a tuple out of the matched list, only the first macth from the left will be stored. 
# - re.findall() : This will help you to search all matching string from left to right when processing a line, where re.search() stops at the first one 
# - re.sub()     : This is used for substituting the values: 
#
# NOTE : If you are looking for a perl way of dealing with regular expression then you should go for 're.search'
#
# We will see each topic in detail later, before that we will see most common patterns which we will use in regular expressions 
#
# * re.match()
# re.match will only will try to match the string at the beginning of the string.
# Mostly when it comes to multi line strings it might ignore the multi lines after the first new line. 
# This usage will be good especially when you want to match only at begininging of the line. 
#
# Syntax : re.match(pattern, string, optional_flag)
#
#        > pattern       : This is the regular expression pattern to be matched.
#        > string        : This is the string which you are processing or you are searching for a pattern at the beginning of the string
#        > optional_flag : These are optional flags which which provided to modify some patterns, these are also called 'modifiers'. 
#
# re.match() function will match a object on success and none on failure. we use group or groups function to retrun the result of the matched object.
#
# . group(num=index_number) : This will be able to return the contents based on the index number in the matched list returned.
# . groups()   : This will be able to retun all matched contents in the list  
#
# Example : Below code will help us to understand about the re.match() 
#
# | import re
# | text  = "God made this wonderful world with lot of puzzles"
# | match = re.match(r'(\s\wo\w.+)', text, re.I)               # Here we are trying to match the string 'wonderful world with lot of puzzles'
# | if match: print match.groups()                                   # We are printing all possible matches with match.groups()
# | else    : print "Nothing found"
#
# NOTE : It is always better before you print the contents of the object make sure the matched object really exist or not, else it will throw an error. 
#      : re.I - This  is the flag and makes the pattern to be case insensitive
#
# * re.search() 
# re.search will help you to search for a pattrn anywere in the string where re.match() help you to search only at the begining of the line. 
# This will perform the search from left to right, but when it finds the very first match its just stops there.
#
# syntax : re.search(pattern, string, optional_flag)
#
#       > pattern       : This is the regular expression pattern to be matched
#       > string        : This is the string wich you are processing to find your pattern, here the entire string will be processed for matches. 
#       > optional_flag : These are optional flags which called as 'modifiers', which will help you to modify the default behaviour of patterns. 
#
# re.search() function will retrun a match object on success and none on failure. 
# We uses the group(num) or groups() method of the matched object to find the matched strings
#
# . group(num=index_number)  : This will return the contents of the string based on the index number from the tuple it produces
# . groups()  : This will be able to return all matching subgroups in the tuple.
#
# Example : Below examplw will demonstrate the usage of re.search
#
# |
# | import re
# | with open('/etc/hosts', 'r') as host_file:
# |   for line in host_file.readlines():
# |     match = re.search(r'\.\w{3}.+m$', line, re.I)
# |     if match: print match.group()
# |     else: print 'No match found'
# | 
#
# * re.search() VS re.match()
# Python provides two primitive regular expressions. 
# re.match  : match checks for any match at the beginning of the string.
# re.search : search checks for match anywere in the string 
#
# Example : Below example will demonstrate the difference between match and search 
#
# |
# | import re
# | line = 'when you com in this world, you are jumping into a very busy world which you cannot stand alone'
# | match_obj  = re.match(r'(\w{4}\s\w{5})', line, re.I|re.M)                   # => This pattern will not return anything since the match is not at the beginning 
# | search_obj = re.search(r'(\w{4}\s\w{5})', line, re.I|re.M)                  # => This pattern will retrun since we used the search method 
# | if match_obj: print match_obj.group()
# | else: print "Regex Error : There is no match found"
# | if search_obj: print search_obj.group()
# | else: print "Regex Error : There is no search found"
# |
#
# * re.findall() - Search all matching patterns
# re.findall() method will help you to find all available matched strings from left to right and it cretaes a list out of it. 
#
# Syntax : re.findall(regex_pattern, string_to_process, optional_flag)
#
# Example : Below example will tell you how to match a regular expression pattern using re.findall()
#
# |
# | import re
# | def find_all_patterns(pattern, string):
# |   match = re.findall(pattern, string, re.I)
# |   if match: print match                                                                    # => here you are not using any group, you are just printing the list
# |   else : print 'No match found !!!'
# | 
# | find_all_patterns(r'(\w+@\w+)', 'ajay291491@gmail.com sent an email to anu275@gmail.com')  # => This will find all email address as part of the strings
# | 
#
# * re.sub() - search and replace 
# One of the effective feature of the re module is its ability to provide substitution. 
# re.sub() module will provide an ability perform substitution operations.
#
# Syntax : re.sub(pattern_to_search, replacing_value, string_to_process, max=<count>)
#
# pattern_to_search : This is the pattern you are going to search with in the string
# replacing value   : This is the value you are going to replace aginst the pattern
# string_to_process : This is the string which you are going to process 
# max               : By default re.sub() will replace all matching pattern, if you give max=count, only that many first matches will only get replaced. 
#
# Example : Below example will show the usage of re.sub
#
# |
# | import re
# | quote = 'Do not dwell in the past, do not think in the future, just live in the present !!!'
# | modified_quote = re.sub(r'\w{7}\s!{3}', 'moment ....', quote)                   # => Here 'present !!!' will change to moment ....'
# | print modified_quote
# |
#
# Example : Below example will show replacing multiple string 
#
# |
# | import re 
# | with open('/etc/hosts', 'r') as host_file:
# |   for line in host_file.readlines():
# |     corrected_url = re.sub(r'(\.com|\.net)', '.org', line)
# |     print corrected_url
# |
#
# * Regular expression modifiers - Optional flags 
# Regular expression modifiers are used to modify the literal meaning of regular expression patterns. 
# These are passed as the optional flag along with the regular expressions and need to use only when required to be mentioned.
# Below are the expression modifiers available in python
# 
# re.I : This will enable case insensitive matching when you pass along with 
# re.L : This interprets the words according to the current locale, but this interpretation will affect the alphbatic word and word boundaries 
# re.M : This will mark the ^ matching at the start of the line rather than string and $ at the end of the line rather than end of the string.
# re.S : Makes a period (dot) match any charector including new line.
# re.U : This interprets the letters according to the charector set, This affects the behavior of the \w, \W, \b and \B
# re.X : This enabled cuter regular expressions, it ignores white spaces (except inside a set [] or escaped by backslash and it treats unescaped '#' as a comment marker 
#
# NOTE : re.I, re.M , re.S and re.X are the common pattern 
#
# * Raw string(r) notation
# In short, to match a literal backslash, one has to write \\ as the RE string, because the regular expression must be \\, and each backslash must be expressed as \\ inside a regular Python string literal. 
# In REs that feature backslashes repeatedly, this leads to lots of repeated backslashes and makes the resulting strings difficult to understand.
#
# The Solution is to use raw string notation for regular expressions, backslashes are not handled in any special way in a string literal. 
# so r"\n" is a two-character string containing '\' and 'n', while "\n" is a one-character string containing a newline. Regular expressions will often be written in Python code using this raw string notation.
# 
# In addition, special escape sequences that are valid in regular expressions, but not valid as Python string literals, now result in a DeprecationWarning and will eventually become a SyntaxError
#
# |
# | Regular_String 	|        Raw_string
# | -----------------------------------------
# |   "ab*" 	        =	  r"ab*"
# |   "\\section"       =	  r"\section"
# |   "\\w+\\s+\\1"     =	  r"\w+\s+\1"
# | -----------------------------------------
#
#
# * Regular expression Patterns 
#
# ^         : Matches at the begining of the line
# $         : Matches at the end of the line 
# .         : This will allow any charector except the new line character, if we are using re.M and optional flag, then it can match new line as well. 
# [...]     : Matches any single character in bracket
# [^...]    : Matches any single character not in bracket
# re*       : Matches 0 or more occurence of the preceeding expression
# re+       : Matches 1 or more of the preceeding expression
# re?       : Matches 0 or 1 occurence of the preceeding expressions 
# re{n}     : Matches exatcly 'n' number of occurence of the preceeding expression
# re{n,}    : Matches 'n' or more than occurence of the preceeding expression
# re{n,m}   : Matches minimum 'n' number of occurence and maximum of 'm' number of occurence
# a|b       : Matches a or b 
# (re)      : groups regular expresions and remembers matched text
# \w        : Matches word character 
# \W        : Matches non word character
# \s        : Matches whitespace 
# \S        : matches non white spaces 
# \d        : Matches digits 
# \D        : matches non-digits 
# \A        : Matches beginning of the string
# \Z        : Matches at the end of the string, if new line exist it ignores the new line
# \z        : Matches end of a string
# \G        : Matches point where last match finished
# \b        : Matches word boundaries where outside brackets, matches backpspace when inside brackets
# \B        : Matches non-word boundaries 
# \n        : Matches new line and carriage return
# \t        : Matches tabs 
# 
# Note      : To understand more pattern and example please visit  below url 
#           https://www.tutorialspoint.com/python/python_reg_expressions.htm
#
# NOTE : Final day of regular expression look at the google video
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 14 - How to work with API
#-------------------------------------------------------------------------------------------------------------
# * HTTP verbs
# There are four http verbs mainly used, their details given below 
#
# - GET           : This retrieves infromation from the specified source.
# - POST          : This sends a new information to the specified source. 
# - PUT           : This updates existing information of a current resource. 
# - DELETE        : Removes existing information from a specified resource. 
# - URI           : Resource name
# - HTTP RESPONSE : status or body
#
# * REST (Representational state transfer)
# REST is an architectural styles that defines a set of constrains and properties.
# REST can be used with any protocols but it generally takes the advantage of the HTTP protocol.
# REST is mainly a resource based rather than action based. 
#
# Below are the 6 main constrains of REST
# - Uniform Interface 
# - Stateless 
# - clinet server
# - Cachable 
# - Layered System
# - Code on demans 
#
# Those API which follows this priciples are called restful api. 
#
# To Study more details about or to understand about the 6 constrains follow below resources 
# URL  : http://www.restapitutorial.com/lessons/whatisrest.html
# Book : 'Undisturbed REST'
#
# * HTTP status codes 
# Before we start dwelling into the deeper aspect of the web modules it is good to understand aboout the https status codes. 
#
# .    100 Continue
# .    101 Switching Protocols
# .    102 Processing
# .
# .    2** Success
# .    200 OK
# .    201 Created
# .    202 Accepted
# .    203 Non-authoritative Information
# .    204 No Content
# .    205 Reset Content
# .    206 Partial Content
# .    207 Multi-Status
# .    208 Already Reported
# .    226 IM Used
# .
# .    3** Redirection
# .    300 Multiple Choices
# .    301 Moved Permanently
# .    302 Found
# .    303 See Other
# .    304 Not Modified
# .    305 Use Proxy
# .    307 Temporary Redirect
# .    308 Permanent Redirect
# .
# .    4** Client Error
# .    400 Bad Request
# .    401 Unauthorized
# .    402 Payment Required
# .    403 Forbidden
# .    404 Not Found
# .    405 Method Not Allowed
# .    406 Not Acceptable
# .    407 Proxy Authentication Required
# .    408 Request Timeout
# .    409 Conflict
# .    410 Gone
# .    411 Length Required
# .    412 Precondition Failed
# .    413 Payload Too Large
# .    414 Request-URI Too Long
# .    415 Unsupported Media Type
# .    416 Requested Range Not Satisfiable
# .    417 Expectation Failed
# .    418 I'm a teapot
# .    421 Misdirected Request
# .    422 Unprocessable Entity
# .    423 Locked
# .    424 Failed Dependency
# .    426 Upgrade Required
# .    428 Precondition Required
# .    429 Too Many Requests
# .    431 Request Header Fields Too Large
# .    444 Connection Closed Without Response
# .    451 Unavailable For Legal Reasons
# .    499 Client Closed Request
# .
# .    5** Server Error
# .    500 Internal Server Error
# .    501 Not Implemented
# .    502 Bad Gateway
# .    503 Service Unavailable
# .    504 Gateway Timeout
# .    505 HTTP Version Not Supported
# .    506 Variant Also Negotiates
# .    507 Insufficient Storage
# .    508 Loop Detected
# .    510 Not Extended
# .    511 Network Authentication Required
# .    599 Network Connect Timeout Error
#
# * General authentication methods available to connect to API
# When you connect to a public API or website, then you do not need to provide an authentication mechanism to connect to an API. 
# But that is normal case when you do with in your organization, so there are several methods you will need to be aware of. 
# Key authentication methods are 
# 
# 1. HTTP Basic authentication 
#    => This is the normal web based authentication mechansim. 
#    => Without SSL support this method is highly insecure. 
#    => With SSL this method can slowdown the process.
#
# 2. API Keys
#   => This is one of the widely used authentication mechanism.
#   => This also has the concern of sending keys as plane text if SSL is not enabled.
#   => This is much faster option compare with the basic http authentication
#   => This is mostly used as an authentiction mechanism ratherthan authorisation
#
# 3. OAuth and OpenID connect 
#   => This is the most secure method available for API standards
#   => This can handle both authentication and authorization
#   => Clearly superior with respect to the security standards compare to other methods
#   => Detailed tutorial available at : https://www.youtube.com/watch?v=CPbvxxslDTU
# 
# To Understand more about these authentication refer : https://nordicapis.com/3-common-methods-api-authentication-explained/
#
# * Key modules to look at when dealing an API from python 
# There are mainly three modules which used in python when it comes to dealing with an API, they are 
# All these modules will try to help you in the same way in the generic concept. 
#
# - urllib  : Module which commonly used in python 3
# - urllib2 : Module which used in python 2, this module is replaced with request module in 2.7
# - request : This is also a module which used in python 2.7
#
# In this chapter we will go through a detailed study only on the 'requests' module since it is the easiest and more efficient tool available 
#
# * Requests()
# Requests is an elegant and simple HTTP library for Python, built for human being
# Requests module is created with few 'PEP 20' idioms which are called as the 'zen of python'. 
# Requests uses 'apache2' licen, that allow your open-source software to be used freely in proprietary, closed-source software.
#
# * How to install 'request' package 
# To install 'request' module, simply run below command in your system. 
#
# | $ pip install requests
#
# * How to make a request
# To make a request, first we will need to import the 'requests' module, once the module is imported then you can perform various operations on this.
# Below is the simple example for making a request.
#
# | import requests
# | connection = requests.get('https://api.github.com/events')
# | print connection.json()
#
# * Making various different type of action with API
# Below are the syntax of using various request types which you can make with the 'requests' module
#
# object = request.get('http://api.github.com/events')
# object = request.post('http://httpbin.org/post', data = {'key': 'value'})
# object = request.put('http://httpbin.org/put', data = {'key': 'value'})
# object = request.delete('http://httpbin.org/delete')
# object = request.head('http://httpbin.org/get')
# object = request.options('http://httpsbin.org/get')
#
# * Passing parameter to the URL
#
# . Passing single parameter
# When you are constructing an url, you can add content to that url in a key value pair and also can retrieve the same using ? and = format
# 
# Syntax : data = {'key': 'value'}
#          requests.post('https://sample_url.com/post', data)
#          requests.get('https://sample_url.com/get?key=value')
#
# . Passing multiple parameter 
# When you are constructing an url with multiple paramter to pass as an argument then you can use below syntax. 
# While retrieving you can use '?' and '=' to join multiple keys values you can use '&' .
#
# Syntax : data = {'key1': 'value1', 'key2': 'value2'}
#          requests.post('https://sample_url.com/post' data)
#          requests.get('https://sample_url.com/get?key1=value1&key2=value2')
#
# . Passing paramater as a list
# You can also pass parameter as a list too, for that you need to follow below syntax. 
# To get the values you will need to use '?' and '=' to construct and '&' to join multiple keys value pairs.
# Also, if multiple values are passed as a list from a key then you need to construct url with multiple '&' on the same key with multiple value
# 
# Syntax : data = {'key1': 'value1', 'key2': ['value2', 'value3']
#          requests.post('https://sample_url.com/post', data)
#          requests.get('https://sample_url.com/get?key1=value1&key2=value2&key2=value3')
# 
# Example : Below example will show us an example about post requests
#
# | 
# | from pprint import pprint 
# | import requests 
# | import re 
# | 
# | main_url = 'http://httpbin.org'
# | single   = {'name': 'Ajay'}
# | couple   = {'husband': 'Ajay' , 'wife': 'Aparna'}
# | family   = {'father': 'Ajay', 'mother': 'Aparna', 'kids': ['Vaiga', 'Rishi']}
# | 
# | def process_post_requests(input_data):
# |   post_url = main_url + '/post'
# |   data_post = requests.post(post_url, input_data)
# |   status = data_post.status_code
# |   if status == 200:
# |    print "Info (post) : Content posted successfully %s" %(input_data)
# |  else: 
# |    print "Fail (post) : Unable to post data"
# |
# | def process_get_requests(input_data):
# |   get_url = main_url + '/get'
# |   sub_url_raw = ""
# |   pair = ""
# |   for keys in input_data:
# |    if type(input_data[keys]) is list:
# |       for element in input_data[keys]:
# |         pair = pair + '&'  + keys + '=' + element  
# |      sub_url_raw = pair + '&'
# |    else:
# |      pair = keys + '=' + input_data[keys] 
# |    sub_url_raw = sub_url_raw + pair + '&'
# |  sub_url = re.sub(r'\&$','', sub_url_raw)
# |  content = requests.get(get_url + '?' + sub_url)
# |  status = content.status_code
# |  print status
# |  if int(status) == 200:
# |    print "Info (get) : Query was successful and content is below **\n"
# |    pprint (content.json())
# |  else:
# |    print "Fail (get) : Query was not successful"
# |
# | def process_requests(input_data):
# |   process_post_requests(input_data)
# |   process_get_requests(input_data)
# |
# | process_requests(single)
# | process_requests(couple)
# | process_requests(family)
# |
#
# * Reading the response content
# Requests itself will talk to the server and will decode the content, most unicode contents are seamlessly decoded. 
# Requests uses the HTTP headers to make the encoding guesses. 
# You can get and set the default encoding using the below synatx. 
#
# Syntax : object.encodig                       => This will get the encoding value 
#        : object.encoding = 'encoding type'    => This will help you to set the encoding 
#
# Request can rereive the data in various different formats such as text, json, raw and binary, their syntax given below 
#
# Syntax : object.text          -> This will return the contect in a text format
#        : object.raw           -> This will not format the data in any format, it just dump the source data 
#        : object.json()        -> This will return the data in a json format if the source support the same
#        : object.content       -> If you have any binary content, then mostly you can use the content method to retrieve the data 
#
# Example : Below example will show you how to get and set the encoding 
#
# | from pprint import pprint 
# | import requests
# | github_url = 'https://api.github.com/events'
# | connection = requests.get(github_url)
# | print connection.encoding
# | connection.encoding = 'ASCII'
# | print connection.encoding
# | pprint (connection.json())
# | print connection.text
# | print connection.raw
# | print connection.content
#
# * Custom Headers 
# You can specify custom headers along with the request with a keyword 'headers' 
# First you will need to create a dictionary with the header infromation and then will need to pass that dictionary to the 'headers' parameter
# 
# Syntax : header_info = { 'key1': 'value1', 
#                          'key2': 'value2'}
#          content = requests.get('https://someurl.com', headers=header_info)
#
# You will need to note below points when you are using custom headers 
# - Custom headers are given less precedence than the more specific information
# - Autherization headers will be overriden if there is parameters specified in '.netrc' which inturn overriden by the auth parametr
# - Autherization parameter will be ignored if you get redirected from the host
# - Proxy authorization headers will be overriden by the proxy credentials provided in the url 
# - Content length headers will be overriden when we can determine the length of the content
#
# * Response headers 
# You can view the http header content from the url using below syntax 
# 
# Syntax  : object.headers
#
# Example : Below example will show us the usage of header 
#
# | import re 
# | import requests
# | from pprint import pprint 
# |
# | url = 'https://api.github.com/events'
# | header_info = {'useragent': 'my-app/0.0.1'}
# | content = requests.get(url, headers=header_info)
# | if content.status_code == 403 : 
# |     print "failed to gather info"
# | else: 
# |    for keys in content.headers:
# |         link_check = re.search(r'^<https://\w.+\.\w{3}', content.headers[keys], re.I|re.M)
# |         if link_check: print "Link : %s" %(link_check.group())
# |         else: print "Do not found use agent"
# 
# * More complicated POST requests
# According to the catagory we can consider post request into different types according to the data itself 
#
# - Data like HTML  : If you have data like HTML then you can simply pass the the contents to the 'data', request will automatically take care of the encoding
#
# | import requests 
# | upload = {'tool': 'puppet'}
# | url = 'http://httpbin.org'
# | connect = requests.post(url + '/post', data=upload)
# | print connect.content
#
# - List and Tuples : This also can be passed aling with the 'data' argument and request will take care of its argument
#
# | import requests
# | url = 'http://httpbin.org'
# | upload = (('key1', 'value1'), ('key2', 'value2')) 
# | connect = requests.post(url + '/post', data = upload)
# | print connect.content
#
# - Json format - [ Continue from there ] 
# When you are dealing with key value pairs or dictionaries, ratherthan you are formatting the data you can always use json to format the data. 
# For using that method you can 'import json' module and then you can use the 'json.dumps' method to process and send the data. 
# While representaing the data to the post request, you can use the 'json' keyword instead of the 'data' or 'files'. 
# Incase you are using 'data' or 'files' argument to pass the dictionary then the json formatting will be lost.
#
# Syntax : Below is the syntax for json format
# 
# import requests 
# import json
# content = {'key' : 'value'}
# connection = requests.post('https://api.github.com/some/endpoint', json=content)
# 
# Example : Below is an example for handling json
#
# | import requests
# | import json
# | 
# | my_url = 'http://httpbin.org'
# | my_dict = { 'name' : 'Rajesh',
# |            'town' : 'kattakada',
# |             'city' : 'Trivandrum',
# |            }
# | 
# | class MyPost(object):
# |
# |  def __init__(self, url, json_data):
# |    self.url = url
# |    self.json_data = json_data
# |
# |   def post_data(self):
# |    connection = requests.post(self.url, json=self.json_data)
# |    if connection.status_code > 200 and connection.status_code < 300:
# |        print "Data uploaded successfully \n %s" %(self.json_data)
# |    else:
# |        print connection.status_code
# |        print "Unable to process data, contact developer"
# |
# | upload = MyPost(my_url, my_dict)
# | upload.post_data()
#
# - Files - Sending a multiparted encoded file 
#
# NOTE : Continue here 
#
#
# NOTE : Continue from http://docs.python-requests.org/en/master/user/quickstart/#
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 15 - Python and Django
#-------------------------------------------------------------------------------------------------------------
# Django is a popular web framework which is available with python. Django also provides a REST API framwork.
# To start working with Django, we will need to install the latest version of the python 3.x. 
# We will now go with a step by step procedure to create an Djnago REST API framework here 
#
# * STEP 1 : Install latest version of the Python and pip
#
# 1. Install python package manager and upgrade it to latest version 
#
# | $ yum install python2-pip
# | $ pip install --upgrade pip
#
# 2. Install python3.x latest using pip 
#
# | $ pip install python3.6
#
# * STEP 2 : Create a virtual environment to work with python 3.x
# 
# 1. Install python vitual environemnt package using pip
#
# | $ pip install virtualenv
# | $ pip install virtualenvwrapper
# 
# 2. Update .bashrc and /etc/profile files with below virtual environment settings for 3.6
#
# | [root@rhceclient01 profile-rest-api]# tail -6  /root/.bashrc 
# | export WORKON_HOME=$HOME/.virtualenvs
# | export PROJECT_HOME=$HOME/Devel
# | export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6
# | export VIRTUALENVWRAPPER_VIRTUALENV=/usr/bin/virtualenv
# | source /usr/bin/virtualenvwrapper.sh
# | [root@rhceclient01 profile-rest-api]#
# | 
# | [root@rhceclient01 profile-rest-api]# tail -6  /etc/profile
# | export WORKON_HOME=$HOME/.virtualenvs
# | export PROJECT_HOME=$HOME/Devel
# | export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6
# | export VIRTUALENVWRAPPER_VIRTUALENV=/usr/bin/virtualenv
# | source /usr/bin/virtualenvwrapper.sh
# | [root@rhceclient01 profile-rest-api]# 
#
# 3. Now create a python virtual envrionment, so that you can work under a isolated 3.6 environment 
#
# | # mkvirtualenv profile_rest_api --python=python3.6 
# | (profile_rest_api) [root@rhceclient01 profile-rest-api]# python -V      => This will show the 3.6 version 
# | Python 3.6.5
# | (profile_rest_api) [root@rhceclient01 profile-rest-api]# 
#
# 4. How to switch on and off from virtual environment 
#
# | (profile_rest_api) [root@rhceclient01 profile-rest-api]# deactivate     => 'deactivate' will drop back to real shell and you can see the python version there 
# | [root@rhceclient01 profile-rest-api]# python -V
# | Python 2.7.5
# | [root@rhceclient01 profile-rest-api]# workon profile_rest_api           => 'workon' on will take you back to the python virtual enviromment 
# | (profile_rest_api) [root@rhceclient01 profile-rest-api]# python -V      
# | Python 3.6.5
# | (profile_rest_api) [root@rhceclient01 profile-rest-api]# 
#
# * STEP 3 : Install 'Django' on the virtual environment 
#
# 1. Install the Djangi 1.11 version 
#
# | (profile_rest_api) [root@rhceclient01 profile-rest-api]# pip3.6 install django==1.11
# | Collecting django==1.11
# |   Downloading https://files.pythonhosted.org/packages/47/a6/078ebcbd49b19e22fd560a2348cfc5cec9e5dcfe3c4fad8e64c9865135bb/Django-1.11-py2.py3-none-any.whl (6.9MB)
# |     100% |████████████████████████████████| 6.9MB 9.1MB/s 
# | Collecting pytz (from django==1.11)
# |   Downloading https://files.pythonhosted.org/packages/30/4e/27c34b62430286c6d59177a0842ed90dc789ce5d1ed740887653b898779a/pytz-2018.5-py2.py3-none-any.whl (510kB)
# |     100% |████████████████████████████████| 512kB 24.2MB/s 
# | Installing collected packages: pytz, django
# | Successfully installed django-1.11 pytz-2018.5
# | (profile_rest_api) [root@rhceclient01 profile-rest-api]#
#
# 2. Install djangorestframework version 3.6.2
#
# | (profile_rest_api) [root@rhceclient01 profile-rest-api]# pip3.6 install djangorestframework==3.6.2
# | Collecting djangorestframework==3.6.2
# |   Downloading https://files.pythonhosted.org/packages/d2/79/e68b85647c539a155c6f6a0738208eb5ed09c61adabfd6f2e6edde944529/djangorestframework-3.6.2-py2.py3-none-any.whl (1.3MB)
# |     100% |████████████████████████████████| 1.3MB 16.0MB/s 
# | Installing collected packages: djangorestframework
# | Successfully installed djangorestframework-3.6.2
# | (profile_rest_api) [root@rhceclient01 profile-rest-api]#
# | 
#
# 3. Verify the package installtion within virtual environment 
#
# | (profile_rest_api) [root@rhceclient01 profile-rest-api]# pip list
# | Package             Version
# | ------------------- -------
# | Django              1.11   
# | djangorestframework 3.6.2  
# | pip                 10.0.1 
# | pytz                2018.5 
# | setuptools          40.0.0 
# | wheel               0.31.1 
# | (profile_rest_api) [root@rhceclient01 profile-rest-api]# 
#
# * STEP 4 : Start a Django Project within the python virtual environment 
# 
#  To create a virtual environment you will need to create a 'src' directory in our vitual environment dirctory and then start the project there as folloes 
#
# | $ pwd
# | /opt/django_project/profile-rest-api
# | $ mkdir src
# | $ ls
# | hello_world.py  README.md  src
# | $ cd src/
# | $ ls
# | django-admin.py startproject profiles_project
# | $ tree profiles_project
# | profiles_project
# | ├── __init__.py
# | ├── __pycache__
# | │   ├── __init__.cpython-36.pyc
# | │   └── settings.cpython-36.pyc
# | ├── settings.py
# | ├── urls.py
# | └── wsgi.py
# |
# | 1 directory, 6 files
# | $ 
# |
#
# * STEP 5 : Start a Django app using'manage.py' script
#
# | $ ls
# | profiles_project
# | $ cd profiles_project/
# | $ ls
# | manage.py  profiles_project
# | $ python manage.py startapp profiles_api
# | $ tree profiles_api/
# | profiles_api/
# | ├── admin.py
# | ├── apps.py
# | ├── __init__.py
# | ├── migrations
# | │   └── __init__.py
# | ├── models.py
# | ├── tests.py
# | └── views.py
# |
# | 1 directory, 7 files
# | $ 
# |
#
# * STEP 6 : Enable apps within 'settings.py' within the 'profiles_project' directory under our project directory
#
# Under the 'INSTALLED_APPS' section in the 'application definition we will need add 3 new item to the list 
#
# . rest_framework              : This will enable the 'rest framework'
# . rest_framework.authtoken    : This will enable a option feature of 'authtoken' 
# . profiles_api                : This will enable the 'profiles_api' apps which we are going to enbale 
#
# | $ cd /opt/django_project/profile-rest-api/src/profiles_project/profiles_project/
# | $ cat settings.py|grep -C13  'Application definition'|tail -14
# | # Application definition
# | 
# | INSTALLED_APPS = [
# |     'django.contrib.admin',
# |     'django.contrib.auth',
# |     'django.contrib.contenttypes',
# |     'django.contrib.sessions',
# |     'django.contrib.messages',
# |     'django.contrib.staticfiles',
# |     'rest_framework',                               -> Here we are appending the list 
# |     'rest_framework.authtoken',                     -> Here we are appending the list 
# |     'profiles_api',                                 -> Here we are appending the list 
# | ]
# | 
# | $
# | 
#
# NOTE : Keep in mind if you want to enable any apps within Django framework, you will need to define that with in 'settings.py' file under the 'INSTALLED_APPS'
#
# * STEP 7 : Create requirement file (Needed only if you are using vagrant)
# Its always a standard practice that we will need to create a 'requirement.txt' file within the project directory, so that we can port our application to a new machine later. 
# 'rerquirement.txt' will contain the information about the package required for our app and also the its version numbers. 
# This file will help to get the package installed for our app, when it gets ported into a new machine. 
# To create the 'requirement.txt' file,  List the number of python package we have installed via pip for the project using 'pip freeze' and store them under the project directory
#
# | $ workon profile_rest_api
# | $ pip3.6 freeze > requirement.txt
# | Django==1.11
# | djangorestframework==3.6.2
# | pytz==2018.5
# | $
#
# * STEP 8 : Update the settings.py with the "ALLOW_HOSTS"
#
# | $ grep HOSTS settings.py 
# | ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '192.168.122.42', 'rhceclient01.svr.apac.sathsang.net',]
# | $ 
#
# * STEP 9 : Start the Django service using 'manage.py' script 
# Once you have completed all above requirements, then you can start your django application. 
# When you start the application you will need to mentioned IP and port from which the webservice can be accessed. 
# Here in our example we will mention the IP as '0.0.0.0' and port as '8080' 
#
# | $ workon profile_rest_api
# | $
# | $ python3.6 manage.py runserver 0.0.0.0:8080            ==> This is how you start a Django server
# | Performing system checks...
# | 
# | System check identified no issues (0 silenced).
# | 
# | You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, authtoken, contenttypes, sessions.
# | Run 'python manage.py migrate' to apply them.
# | 
# | July 17, 2018 - 14:26:21
# | Django version 1.11, using settings 'profiles_project.settings'
# | Starting development server at http://0.0.0.0:8080/
# | Quit the server with CONTROL-C.
# | [17/Jul/2018 14:26:25] "GET / HTTP/1.1" 200 1716        ==> This is the output you will get in log when you access the website
# | [17/Jul/2018 14:26:32] "GET / HTTP/1.1" 200 1716
# | [17/Jul/2018 14:26:33] "GET / HTTP/1.1" 200 1716
#
# * STEP 10 : Verify you can access the webpage 
#
# | [root@sathsang python]# elinks http://rhceclient01.svr.apac.sathsang.net:8080
# | Welcome to Django 
# | It worked!                                                                                                     
# |                                                                                                                                                                                                             
# | Congratulations on your first Django-powered page.                                                                                                                                                          
# | Next, start your first app by running python manage.py startapp [app_label].                                                                                                                                
# | You're seeing this message because you have DEBUG = True in your Django settings file and you haven't configured any URLs. Get to work!                                                                     
# |
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 16 - Python and database
#-------------------------------------------------------------------------------------------------------------
#
# 
#-------------------------------------------------------------------------------------------------------------
# Chapter 17 - Common untilities and its use 
#-------------------------------------------------------------------------------------------------------------
#
# * pprint - pretty printer 
# pprint() module is normally used to print raw data in formatted syntax, so that it is much more readable than the raw data 
#
# Syntax : from pprint import pprint 
#          pprint ("data_to_print")
#
# Example : Below is an example for pprint 
#
# | from pprint import pprint
# | import requests
# |
# | def get_data(url):
# | 
# |   counter = 0
# |   connection = requests.get(url)
# |   data_snap = connection.json()
# |   for item in data_snap:
# |     counter += 1
# |     if counter < 2:
# |       data_one = {}
# |       data_one = item
# |       for key in data_one.keys():
# |         pprint (data_one[key])
# | 
# | get_data('https://api.github.com/events')
# |
#
#
#
# . https://developers.google.com/edu/python/utilities
# . https://docs.python.org/2/howto/logging.html
# . Try and exception method
# . https://www.youtube.com/watch?v=uKZ8GBKmeDM
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 18 - Writing test cases in python
#-------------------------------------------------------------------------------------------------------------
#
# https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
#
#-------------------------------------------------------------------------------------------------------------
