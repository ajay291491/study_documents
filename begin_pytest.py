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
# NOTE : Start from '2. Example for TDD session'
#
#
#



