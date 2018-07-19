#-------------------------------------------------------------------------------------------------------------
#
#                                           Python and Django
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 1 : Setting up a Django environment
#-------------------------------------------------------------------------------------------------------------
# Django is a popular web framework which is available with python. Django also provides a REST API framwork.
# To start working with Django, we will need to install the latest version of the python 3.x. 
# We will now go with a step by step procedure to create an Djnago REST API framework here 
#
# - STEP 1 : Install latest version of the Python and pip
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
# - STEP 2 : Create a virtual environment to work with python 3.x
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
# - STEP 3 : Install 'Django' on the virtual environment 
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
# - STEP 4 : Start a Django Project within the python virtual environment 
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
# - STEP 5 : Start a Django app using'manage.py' script
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
# - STEP 6 : Enable apps within 'settings.py' within the 'profiles_project' directory under our project directory
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
# - STEP 7 : Create requirement file (Needed only if you are using vagrant)
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
# - STEP 9 : Start the Django service using 'manage.py' script 
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
# - STEP 10 : Verify you can access the webpage 
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
# Chapter 2 : Django Data Models
#-------------------------------------------------------------------------------------------------------------
# Models is the single definitive source of data you are storing. It contains the type and behavious of the data you are storing. 
# In django we uses 'models' to describe the data we need for our application, django then uses these models to describe tables needed. 
# Generally each data type will store into a single database table. In django we specify each data to use some type available in the database table.
# Baceuse of this Django  will use 'mode;s' to take care of working with the backend database so that we don't need to interact with any DB or sql queries.
#
# * Defining modles using 'modles.py'
# When you create an application using django 'python manage.py startapp  <apps_name>', then there will be a 'modles.py' file gets created within apps directory
# Below is a sample file you can see, and how to update this file will discusses further. 
#
# | $ pwd
# | /opt/django_project/profile-rest-api/src/profiles_project/profiles_api   ==> Here 'profiles_api' is the application name 
# | $ ls -l 
# | total 20
# | -rw-r--r--. 1 root sathsang 63 Jul 14 19:55 admin.py
# | -rw-r--r--. 1 root sathsang 98 Jul 14 19:55 apps.py
# | -rw-r--r--. 1 root sathsang  0 Jul 14 19:55 __init__.py
# | drwxr-sr-x. 3 root sathsang 44 Jul 17 08:59 migrations
# | -rw-r--r--. 1 root sathsang 57 Jul 14 19:55 models.py
# | drwxr-sr-x. 2 root sathsang 94 Jul 17 08:59 __pycache__
# | -rw-r--r--. 1 root sathsang 60 Jul 14 19:55 tests.py
# | -rw-r--r--. 1 root sathsang 63 Jul 14 19:55 views.py
# | $ cat models.py
# | from django.db import models
# | 
# | # Create your models here.
# | (profile_rest_api) [root@rhceclient01 profiles_api]# 
# |
# | $
#
# NOTE : You can refer below url to understand about various fileds available with django
# URL  : https://docs.djangoproject.com/en/2.0/ref/models/fields/
# 
# * Creating a user profile model
# This is the basic model we will need to create in our django so that we can manage users. When we create a user profile we will need to think about three different things here. 
#
# . Creatin a user
# . Manging a user 
# . Deleting a user
#
# Before we begin, we will need to understand few modules which we will be using while creating a 'user profile model' 
#
# . from django.db import models                                =>  https://docs.djangoproject.com/en/2.0/topics/db/models/ (used for defining models)
# . from django.contrib.auth.models import AbstractBaseUser     =>  https://docs.djangoproject.com/en/2.0/ref/contrib/auth/ (This will provide the base use profile)
# . from django.contrib.auth.models import PermissionsMixin     =>  https://docs.djangoproject.com/en/2.0/ref/contrib/auth/ (This will provide the ability to give permission for user)
#
# PENDING : This Lecture is half way (19. Add a user model manager)
#           . We have imported the required modules
#           . We have define Userprofile class and its variables and functions 
#           . Continue from '19. Add a user model manager'
#
