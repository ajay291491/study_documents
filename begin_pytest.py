#-------------------------------------------------------------------------------------------------------------
# Chapter 1 - Test driver development (TDD)
#-------------------------------------------------------------------------------------------------------------
# * Introduction 
# Test driven development is used to keep your codebase error or bug free so that you can work with clean code. 
# Having a buggy code base will cause problems to the development teams. 
# Due to a buggy codebase they may not be able to concentrate on the feature development and will end up in fixing the older codes.
# To deal with such situations, it is always a best practice to learn TDD which will help to eleminate this problem
#
# TDD works in the functions and classes level and they goes through the positives and negatives of your code.
# TDD is a practice of writing the unit tests before you write the production codes. 
# This has many benifits, even though it is bit back wards 
#
# - It can make sure every line of production code is working as soon as it is written. 
# - if there is a problem it is easy to fix since you had written only small amount of code from last time it is executed for testing. 
# - TDD will give you and your team confidence to change the code immeditelty as soon as you see anything broken in your codebase. 
# - It follows a principle of RED -> GREEN -> REFACTOR 
#
# This course will deal with the step by step procedure to deal with the unit testing and test case scenarios 
#
# * why Unit test 
# - They are the first safety nets for catching bugs before they get into the field
# - Unit test validates test case for each individual functions 
# - They should build and run the developr's development environment 
# - Unit tests should run fast 
#
#
# * Levels of Testing
# . Unit testing        - Testing at the function level
# . Component testing   - Testing is at the library and compiled binary level
# . System testing      - Tests external interface of a system which is a collection of sub systems 
# . Performance testing - Test done on subsystem and system level to verify the timimg and resource usage are acceptible
#
# * Overview of unit testing 
# TDD ensures you are writing a high qulity and bug free code 
# 
# . This is a process where developer takes a personal responsibility for the quality of the code.
# . This process is driven by writing the unit tests before the production code. 
# . Do not write all the tests or production code at the very first 
# . Tests and production code both written in small bits of functionality. 
#
# * Benefits of unit testing 
# Below are some key beninifits of TDD 
# 
# . This gives you the confidence to change the code as soon as something is broken. 
# . This confidence comes from the immediete feedback from the test case on each change done on the production code.
# . Test documents what the production code is doing, so that other developer can easily understand what the code is doing. 
# . It drives to good object oriented design which will break the dependacies. 
#
# * TDD workflow
# TDD workflow devided into four phases, RED, GREEN, REFACTOR and REPEAT
#
# . RED      - In the Red phase you will write a failing unit tests for the next bit of production codes you are going to write.
# . GREEN    - This Phase you will write a set of production code which will make failing unit test to pass. 
# . REFACTOR - At this phase we cleaup the unit test in the production code to make sure your team follows the proper coding stadards and no duplication in the code base. 
# . REPEAT   - At this phase you REPEAT above three steps until you find your code completely clean
#
# * Laws of TDD
# Below are the laws of TDD which you  need to follow while writing a code
#
# . You may not write any production code until you write a failing unit test
# . If your unit test fails before you write a production code, that means your unit test is written properly
# . You may not write more of a unit test than it is sufficient to fail, this forces you to write only enough of test case for next test case. 
# . You may not write more of a production code which is not sufficient to pass the current test case. 
#
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 2 - Overview of pytest
#-------------------------------------------------------------------------------------------------------------
#
# * What is pytest
# Below are the keys things about pytest 
#
#  . Pytest is a python unit testing framework
#  . It provides ability to create tests functions, test modules, test fixtures and test classes 
#  . Uses the built in python assert statement 
#  . Also provides commandline parameters and utilities to understand what tests are executed in what order and also you can filter the output
#
# * How to create a Test using pytest
# When you create a test case in python you will need to follow certain guidelines 
# 
# . Tests are python function which begins with 'test_' at the beginning of the function name 
#   | Example : def test_my_function():'
#
# . Tests do verification of values using the standard python assert statement.
#   | Example : below is sample test case 
#   | def test_my_function(value): 
#   |     assert value == 1
#
# . Similar tests can be grouped together by including them in similar class or module 
#
# * Pytest - command
# We can use the pytest command utility to run the unit tests from a commandline. 
# This will give us the output in green if the test is OKAY and it will be giving RED if the test is failed. 
#
# Example : Below is a sample program we had written to test the unit test case for a program to find the multiple of 3. 
#
# | #!/usr/bin/python
# | #
# | import pytest
# | 
# | def check_multiple_of_three(number):
# |     if (number % 3) == 0:
# |         return "Yes"
# | 
# | def test_check_function():
# |     retValue = check_multiple_of_three(5)
# |     assert  retValue == "Yes"
# | 
#
# NOTE : Below is the first run we are trying to run a RED Phase
# 
# | [root@sathsang py_test]# pytest -v unit_test_one.py 
# | ==================================== test session starts ========================================================================================================================
# | platform linux2 -- Python 2.7.13, pytest-3.7.1, py-1.5.4, pluggy-0.7.1 -- /usr/bin/python
# | cachedir: .pytest_cache
# | rootdir: /study_docs/python/py_test, inifile:
# | collected 1 item                                                                                                                                                                                            
# | 
# | unit_test_one.py::test_check_function FAILED     [100%]
# | ================================================ FAILURES ==============================================================================================================================
# | ______________________ test_check_function ________________________________________________________________________________________________________________________
# |
# |    def test_check_function():
# |        retValue = check_multiple_of_three(5)
# | >       assert  retValue == "Yes"
# | E       AssertionError: assert None == 'Yes'
# | 
# | unit_test_one.py:13: AssertionError
# | ============================ 1 failed in 0.05 seconds ======================================================================================================================
# | [root@sathsang py_test]# 
#
# NOTE : Now we are running a GREEN phase by making the code pass
# 
# | [root@sathsang py_test]# pytest -v unit_test_one.py 
# | ================================================================= test session starts ========================================================================================================================
# | platform linux2 -- Python 2.7.13, pytest-3.7.1, py-1.5.4, pluggy-0.7.1 -- /usr/bin/python
# | cachedir: .pytest_cache
# | rootdir: /study_docs/python/py_test, inifile:
# | collected 1 item                                                                                                                                                                                    
# | unit_test_one.py::test_check_function PASSED  [100%]
# | 
# | =========================================================== 1 passed in 0.03 seconds ======================================================================================================================
# | [root@sathsang py_test]# 
#
# NOTE : Now we know why our code was failing in the RED phase and we will do REFACTOR to fix the code 
#
# | import pytest
# | 
# | def check_multiple_of_three(number):
# |     if (number % 3) == 0:
# |         return "Yes"
# |     else:
# |         return "Not"
# | 
# | def test_success_function():
# |     retValue = check_multiple_of_three(9)
# |     assert  retValue == "Yes"
# | 
# | def test_failure_function():
# |     retValue = check_multiple_of_three(5)
# |     assert  retValue == "Not"
# | 
#
# NOTE : Now we are moving to the repeat phase 
#
# | [root@sathsang py_test]# pytest -v unit_test_one.py 
# | ============================================================= test session starts ========================================================================================================================
# | platform linux2 -- Python 2.7.13, pytest-3.7.1, py-1.5.4, pluggy-0.7.1 -- /usr/bin/python
# | cachedir: .pytest_cache
# | rootdir: /study_docs/python/py_test, inifile:
# | collected 2 items                                                                                                                                                                                           
# |
# | unit_test_one.py::test_success_function PASSED      [ 50%]
# | unit_test_one.py::test_failure_function PASSED      [100%]
# | 
# | ===================================================== 2 passed in 0.04 seconds ======================================================================================================================
# | [root@sathsang py_test]# 
#
#
# * Test Discovery
# This is the process where pytest automatically detects the unit tests from a python program. 
# For python to find test program, it need to be of either of the below catagory
# 
# . Pytest will automatically discover the program when you execute based on a standard naming convention
# . Test function must include 'test' at the beginning of the function name, i.e like 'def test_even_numbers():'
# . Classes should start with 'Test' at the biginning of the class and should not contain '__init__' method, i.e like 'class Test_Number_Series():'
# . Filenames of test module should start and end with 'test', i.e like test_my_numbers.py or number_test.py
#
# --------------------------------------------------
#   Type   |   Naming conventions     |   Supported 
# --------------------------------------------------
# Function     test_my_numbers():            Yes
# Function     test_my_output():             Yes
# Function     my_test_number():              No
# Function     my_test_output():              No
# Class        Test_My_Numbers():            Yes
# class        Test_My_Logic():              Yes
# class        My_Test_Number():              No
# class        My_Test_output():              No
# file         test_my_numbers.py            Yes
# file         my_numbers_test.py            Yes
# file         my_test_numbers.py             No
#----------------------------------------------------
#
#
# * Xunit setup and teardown functions 
# One keys feature provided by all unit tests is running the setup code before and after the test. 
# Pytest provides this functionality by Xunit setup and teardown function and with pytest fixtures. 
#
# Xunit teardown will help you run the codes before and after in below catagories 
# . Test modules 
# . Test functions 
# . Test classes 
# . Test method in test classes
#
# def setup_module():
# def teardown_module():
#
# def setup_functions():
# def teardown_functions():
#
# def setup_classes():
# def teardown_classes():
#
# def setup_method():
# def teardown_method():
#
# NOTE : Using these setup and teardown functions help reduce the code duplication by letting you to specify the setup and teardown functions once at each level as necessary. 
#        This will help to avoid maniting the code at the individual unit tests and this will help to keep you code clean. 
#
# Continue : Xunit setup and teardown functions and practicals 
#


