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
# | $ workon profile_rest_api
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
# STEP 1 : Creating custom user model and user model manager with in our app
#
# Before we begin, we will need to understand few modules which we will be using while creating a 'user profile model' 
#
# . from django.db import models                                =>  https://docs.djangoproject.com/en/2.0/topics/db/models/ (used for defining models)
# . from django.contrib.auth.models import AbstractBaseUser     =>  https://docs.djangoproject.com/en/2.0/ref/contrib/auth/ (This will provide the base use profile)
# . from django.contrib.auth.models import PermissionsMixin     =>  https://docs.djangoproject.com/en/2.0/ref/contrib/auth/ (This will provide the ability to give permission for user)
# . from django.contrib.auth.models import BaseUserManager      =>  https://docs.djangoproject.com/en/2.0/ref/contrib/auth/ (This will provide the basic user profile to be used)
#
# Below is the sample 'model.py' which we created for the 'profile_api' application
#
# | $ workon profile_rest_api
# | $ pwd
# | /opt/django_project/profile-rest-api/src/profiles_project/profiles_api
# | $ vim models.py 
# | from django.db import models
# | from django.contrib.auth.models import AbstractBaseUser
# | from django.contrib.auth.models import PermissionsMixin
# | from django.contrib.auth.models import BaseUserManager
# | 
# | # Create your models here.
# | 
# | class UserProfileManager(BaseUserManager):
# |     """ Helps Django to work with the custom user profile which we created """
# | 
# |     def createuser(self, email, name, password=None):
# |         """ Helps to create a new user profile objects """
# |         
# |         if not email:
# |             raise ValueError('User must have an email address')
# |         elif not name:
# |             raise ValueError('User must have a name specified')
# | 
# |         # This will normalize the email by setting everything to lowercase 
# |         email = self.normalize_email(email)
# | 
# |         # This will create a normal user with the provided information
# |         user  = self.model(email=email, name=name)
# |         
# |         # This will set the password and store it in database as a hash
# |         user.set_password(password)
# | 
# |         # This will save the user details in the database 
# |         user.save(using=self.db)
# | 
# |         return user
# | 
# |    def create_superuser(self, email, name, password): 
# |        """ Creates a super user with the given details """
# | 
# |        # Using the same 'createuser' function defined within the class to create the user
# |        user = self.createuser(email, name, password)
# |  
# |        # Set the user as a Super user and add to group staff
# |        user.is_superuser = True
# |        user.is_staff     = True 
# |        
# |        # Save the user and retun the user details 
# |        user.save(using=self._db)
# |        retrun user
# | 
# | 
# | class UserProfile(AbstractBaseUser, PermissionsMixin):
# |     """ Represents 'user profile' inside our system and inherited form AbstractBaseUser and PermissionsMixin """
# | 
# |     email     = models.EmailField(max_length=255, unique=True) 
# |     name      = models.CharFiled(max_length=255)
# |     is_active = models.BooleanField(default=True)
# |     is_staff  = models.BooleanFiled(default=False)
# | 
# |    
# |     # Object manager (This will be covered in next lesson)
# |     objects = UserProfileManager()
# |    
# |     # Standard djano fileds for user profle 
# |     USERNAME_FIELD  = 'email'
# |     REQUIRED_FILEDS = ['name']
# |     
# |     def get_full_name(self):
# |         """ Used to get a user full name """
# | 
# |         return self.name
# | 
# |     def get_short_name(self):
# |         """ Used to get the short name """
# | 
# |         return self.name 
# | 
# |     def __str__(self):
# |         """ Django uses this function when it needs to convert the object to a string this is manadatory """
# | 
# |         return self.email
# |      
#
# STEP 2 : Update the settings.py in our project to use the custom user model
# To enable this you will need go to the project directory and update the 'settings.py' to refer to the custom user model which we created. 
# By enabeling the custom user profile we are overriding the default user profile model in django
# Value you need to enable is 'AUTH_USER_MODEL = profiles_api.UserProfile', by mentioning this django understand it is coming from the profile_api apps models.py  
#
# Example : Below is the sample of this output
#
# | $ pwd
# | /opt/django_project/profile-rest-api/src/profiles_project/profiles_project
# | $ grep -i AUTH_USER_MODEL settings.py 
# | AUTH_USER_MODEL = 'profiles_api.UserProfile'
# | $
#
# STEP 3 : Create Migration and sync DB
# Using this we are going to update the changes we did to the django database. 
# This is done using without any sql queries, this migration is does by django itself in the background seemlessly. 
# This migration process will include two stages 
# 
# 1. Prepare for Migration 
# 2. Perform Migration 
#
# 1. Prepare for Migration : At this stage you will need to use the 'manage.py' within our project using command 'makemigrations' 
#                          : Once you have run the command django will prepare the migration file, which can be used for migration in next step
#
# | 
# | $ workon profile_rest_api
# | $ python manage.py makemigrations 
# | Migrations for 'profiles_api':
# |   profiles_api/migrations/0001_initial.py       => You can look at this file to understand the details about migration (at the app base location)
# |    - Create model UserProfile
# | $
# |
# 
# 2. Perform Migration : Once you have validated the migration file at 'profiles_api/migrations/0001_initial.py' and happy with the changes its going to make. 
#                      : Then the next step to run the actual migraton, this will go and alter the database with required changes needed for our requirement 
#
# | $ python manage.py migrate
# | Operations to perform:
# |   Apply all migrations: admin, auth, authtoken, contenttypes, profiles_api, sessions
# | Running migrations:
# |   Applying contenttypes.0001_initial... OK
# |   Applying contenttypes.0002_remove_content_type_name... OK
# |   Applying auth.0001_initial... OK
# |   Applying auth.0002_alter_permission_name_max_length... OK
# |   Applying auth.0003_alter_user_email_max_length... OK
# |   Applying auth.0004_alter_user_username_opts... OK
# |   Applying auth.0005_alter_user_last_login_null... OK
# |   Applying auth.0006_require_contenttypes_0002... OK
# |   Applying auth.0007_alter_validators_add_error_messages... OK
# |   Applying auth.0008_alter_user_username_max_length... OK
# |   Applying profiles_api.0001_initial... OK
# |   Applying admin.0001_initial... OK
# |   Applying admin.0002_logentry_remove_auto_add... OK
# |   Applying authtoken.0001_initial... OK
# |   Applying authtoken.0002_auto_20160226_1747... OK
# |   Applying sessions.0001_initial... OK
# | (profile_rest_api) [root@rhceclient01 profiles_project]# 
#
# Once you have completed the migraition, you will see a database file on the project base location as below 
#
# | $ pwd
# | /opt/django_project/profile-rest-api/src/profiles_project
# | $ ls -l db.sqlite3
# | -rw-r--r--. 1 root sathsang 44032 Jul 20 05:30 db.sqlite3
# | $ file db.sqlite3
# | db.sqlite3: SQLite 3.x database
# | $ 
# 
# If you migrate already then you run the migrate command again then it will say there is no more migration pending until we upate any. 
#
# | $ python manage.py migrate
# | Operations to perform:
# |   Apply all migrations: admin, auth, authtoken, contenttypes, profiles_api, sessions
# | Running migrations:
# |   No migrations to apply.
# | $ 
# |
#
# STEP 4 : Create a Django super user 
# Django createsuperuser fascility will help to create a superuser which cane make use of the custom user model we have created 
#
# | $ workon profile_rest_api
# | $ python manage.py createsuperuser
# | Email: ajay291491@gmail.com 
# | Name: Ajayaghosh V L
# | Password: 
# | Password (again): 
# | Superuser created successfully.
# | $ 
#
# STEP 5 : Register user model with Django admin
# In this topic we will register the user profile model with the django admin. 
# This will help us to manage the user profile objects from the django admin. 
#
# |
# | $ workon profile_rest_api 
# | $ pwd
# | /opt/django_project/profile-rest-api/src/profiles_project/profiles_api
# | $ ls -l
# | total 20
# | -rw-r--r--. 1 root sathsang  251 Jul 23 18:55 admin.py
# | -rw-r--r--. 1 root sathsang   98 Jul 14 19:55 apps.py
# | -rw-r--r--. 1 root sathsang    0 Jul 14 19:55 __init__.py
# | drwxr-sr-x. 3 root sathsang   67 Jul 22 08:12 migrations
# | -rw-r--r--. 1 root sathsang 2585 Jul 23 18:26 models.py
# | drwxr-sr-x. 2 root sathsang   94 Jul 23 18:55 __pycache__
# | -rw-r--r--. 1 root sathsang   60 Jul 14 19:55 tests.py
# | -rw-r--r--. 1 root sathsang   63 Jul 14 19:55 views.py
# | $ vim admin.py 
# | from django.contrib import admin            # => This will import the admin module which needed to resiter our custom user profile
# | from . import models		        # => This will import the model from the same apps directory
# | 
# | Register your models here.
# | admin.site.register(models.UserProfile)     # => This will register the 'UserProfile' to the django admin using the 'admin.site.register' module
# | $ 
# | 
#
# STEP 6 : Test you django admin login 
# Once you have completed till step 5, then you can test Django superuser login for, 
# 
# 1. Start the django server if not running already 
# 2. Login to Django admin page http://rhceclient01.svr.apac.sathsang.net:8080/admin/
# 3. Use the email address and password which you have used to create the super user
# 4. Once you have logged in You should be able to see the superuser profile as below 
#    - Site administration
#       - AUTH TOKEN
#       - AUTHENTICATION AND AUTHORIZATION
#       - PROFILES_API
# 
#-------------------------------------------------------------------------------------------------------------
# Chapter 3 : Django REST Framework Views - APIView
#-------------------------------------------------------------------------------------------------------------
# Django REST framework offers two different helper ways to create our own API end points 
#
# 1. APIView
# 2. Viewset
#
# Both ways are slightly different and offers their own benifit. 
# In this chapter we will take a close look at the 'APIView' framework.  
#
# * APIView 
# APIView allows us to find the stadard HTTP methods such as 
#
# - GET     : This helps you to get the details of one or more resources 
# - PUT     : This helps you to create a new resource
# - POST    : This helps you to update an existing item 
# - PATCH   : This helps you to partially update an existing item
# - DELETE  : This help you to delete a resource 
#
# This helps to given most application control over logic using various methods used above. 
#
# * When to use APIView 
# Below are the few use case scenarios or examples where you can use the APIViews 
#
# - Perfect for building a complex logics, which means rather than just updating a resourcce, you can have more complex logics 
# - When you need full control over your application logic 
# - Processing application files and expecting a synchronous response on the same request 
# - When you are calling other APIs or Services in the same request 
# - While accessing local files or data
#
# * Basics of How to create a APIView 
# Before we jump into deploying an API we can go through the basics of how to create an API. 
# In this chapter we will discuss the step by step procedure for creating an API view 
#
# -------- <<< STEP 1 - 3 dealing with the [GET] method >>> ----------
# 
# STEP 1 : Creating views for your API (For GET method) 
# To create views you will need to navigate to your application base directory and then you will need to make the necessary updates in views.py file 
# This is the file which basically create the view for the application API end point which user visits 
#
#
# | $ workon profile_rest_api
# | $ pwd
# | /opt/django_project/profile-rest-api/src/profiles_project/profiles_api
# | $ ls -l 
# | total 20
# | -rw-r--r--. 1 root sathsang  377 Jul 23 19:05 admin.py
# | -rw-r--r--. 1 root sathsang   98 Jul 14 19:55 apps.py
# | -rw-r--r--. 1 root sathsang    0 Jul 14 19:55 __init__.py
# | drwxr-sr-x. 3 root sathsang   67 Jul 22 08:12 migrations
# | -rw-r--r--. 1 root sathsang 2585 Jul 23 18:26 models.py
# | drwxr-sr-x. 2 root sathsang   94 Jul 23 19:05 __pycache__
# | -rw-r--r--. 1 root sathsang   60 Jul 14 19:55 tests.py
# | -rw-r--r--. 1 root sathsang  936 Jul 25 21:50 views.py
# | $ vim views.py 
# | 
# | from django.shortcuts import render
# | 
# | from rest_framework.views import APIView            # This imports the APIView class from the django rest_framework views 
# | from rest_framework.response import Response        # This will process output which we need to return in JSON format with status codes 
# | 
# | # Create your views here.
# | 
# | class HelloApiView(APIView):
# |     """ Test API View """
# | 
# |     def get(self, request, format=None):
# |         """ Returns a list of APIView Features """
# | 
# |         an_apiview = [
# |             'Uses HTTP methods as functions (get, post, patch, put , delete)',
# |             'It is similar to traditional Django view',
# |             'Gives you the most control over your application logic', 
# |             'Its manually mapped to URLs']
# | 
# |         # response has to be always send it a dictionary format, for that we will associate our list with a key as seen below 
# |         return Response({'Message' : 'Hello, welcome to Ajay\'s first api endpoint', 'an_apiview': an_apiview })
# | 
# | 
#
# STEP 2 : Configure View URL (For GET method) 
# To Configure a view url you have to configure the 'URL dispatcher' and there is two steps of process behind this.
#
# 1. Configure - url.py (Under Project Base Directory): 
#      Update the url.py within the project directory, which is first place Django will look at while request comes in. 
#      At this location you will enable a pointer to the application based url file. 
#      When the requests comes in this url.py will forward the request to the application based url.py and from there request will be further processd. 
#
# | 
# | $ workon profile_rest_api
# | $ cat urls.py 
# | """profiles_project URL Configuration
# | 
# | The `urlpatterns` list routes URLs to views. For more information please see:
# |     https://docs.djangoproject.com/en/1.11/topics/http/urls/
# | Examples:
# | Function views
# |     1. Add an import:  from my_app import views
# |     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# | Class-based views
# |     1. Add an import:  from other_app.views import Home
# |     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# | Including another URLconf
# |     1. Import the include() function: from django.conf.urls import url, include
# |     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
# | """
# | from django.conf.urls import url
# | from django.conf.urls import include   #  This is the module which import to forward request to apps based url.py
# | from django.contrib import admin
# | 
# | urlpatterns = [
# |     url(r'^admin/', admin.site.urls),
# | 
# |    # Below will forward the request to /opt/django_project/profile-rest-api/src/profiles_project/profiles_api/views.py 
# |    # When there is a query landed on url : http://rhceclient01.svr.apac.sathsang.net:8080/api/ """
# |     url(r'^api/', include('profiles_api.urls'))
# | ]
# | $ 
# | 
#
# 2. Configure - url.py (Under Application Base Directory):
#      In Most of the cases there won't be any url.py file in the application base directory and you might need to create one. 
#      Once the request formwarded to the application based 'url.py' then it will look for the 'url_pattern' list for the definition 
#      In the url_pattern we will use the 'url' module to access 'views.py' and provide the definition as the output 
#
# | $ pwd
# | /opt/django_project/profile-rest-api/src/profiles_project/profiles_api
# | $
# | $ ls -l 
# | total 24
# | -rw-r--r--. 1 root sathsang  377 Jul 23 19:05 admin.py
# | -rw-r--r--. 1 root sathsang   98 Jul 14 19:55 apps.py
# | -rw-r--r--. 1 root sathsang    0 Jul 14 19:55 __init__.py
# | drwxr-sr-x. 3 root sathsang   67 Jul 22 08:12 migrations
# | -rw-r--r--. 1 root sathsang 2585 Jul 23 18:26 models.py
# | drwxr-sr-x. 2 root sathsang  149 Jul 28 21:07 __pycache__
# | -rw-r--r--. 1 root sathsang   60 Jul 14 19:55 tests.py
# | -rw-r--r--. 1 root sathsang  423 Jul 28 21:07 urls.py
# | -rw-r--r--. 1 root sathsang 1226 Jul 28 19:58 views.py
# | $
# | $ cat views.py 
# | from django.shortcuts import render
# | 
# | from rest_framework.views import APIView		# This imports the APIView class from the django rest_framework views 
# | from rest_framework.response import Response	# This will process output which we need to return in JSON format with status codes 
# | 
# | # Create your views here.
# | 
# | class HelloApiView(APIView):
# |     """ Test API View """
# |     
# |     def get(self, request, format=None):
# |         """ Returns a list of APIView Features """
# | 
# |         an_apiview = [
# |             'Uses HTTP methods as functions (get, post, patch, put , delete)',
# |             'It is similar to traditional Django view',
# |             'Gives you the most control over your application logic', 
# |             'Its manually mapped to URLs'
# |         ]
# | 
# |         family_details = {
# |             'Father'   : 'Ajayaghosh V L',
# |             'Mother'   : 'Aparna A',
# |             'Daughter' : 'Vaiga Shanti A',
# |             'Son'      : 'Rishi Krishna A',
# |         }
# | 
# | 
# |         # response has to be always send it a dictionary format, for that we will associate our list with a key as seen below 
# |         return Response({'Message' : 'Hello, welcome to Ajay\'s first api endpoint', 'an_apiview': an_apiview, 'family_details' : family_details })
# | 
# | $
# | $ more urls.py 
# | from django.conf.urls import url	# This module is to handle the url
# | from . import views			# We are importing views.py in our apps base directory here 
# | 
# | urlpatterns = [ 
# |     
# |     # Using the url module, we are defining the api view 'hello-view/'
# |     # hello-view will display the get method defined under the HelloApiView class under the 'views.py' as the view
# |     url(r'^hello-view/', views.HelloApiView.as_view()),	
# |     ]
# | $ 
# | $
# | 
#
# STEP 3 : Connect to your API and try to get the 'hello-view/' api view (For GET method) 
# Login to any host and run belowscript to connect to the API which you have just created and try to get the data 
#
#
# | # [root@sathsang sample_scripts]# cat test_get_hello_api.py
# | #!/usr/bin/python
# | #
# | # Script to check the working status of hellp.api
# | #
# | 
# | from pprint import pprint
# | import requests 
# | 
# | #
# | main_url = 'http://rhceclient01.svr.apac.sathsang.net:8080/api/'
# | sub_url  = 'hello-view/'
# | #
# | def get_api_content(bae_api, api_key):
# |     
# |     full_url = bae_api + api_key
# |     connect = requests.get(full_url)
# |     pprint (connect.json())
# | 
# | get_api_content(main_url, sub_url)
# | 
# | [root@sathsang sample_scripts]# python test_get_hello_api.py
# | {u'Message': u"Hello, welcome to Ajay's first api endpoint",
# |  u'an_apiview': [u'Uses HTTP methods as functions (get, post, patch, put , delete)',
# |                  u'It is similar to traditional Django view',
# |                  u'Gives you the most control over your application logic',
# |                  u'Its manually mapped to URLs'],
# |  u'family_details': {u'Daughter': u'Vaiga Shanti A',
# |                      u'Father': u'Ajayaghosh V L',
# |                      u'Mother': u'Aparna A',
# |                      u'Son': u'Rishi Krishna A'}}
# | [root@sathsang sample_scripts]# 
# | 
#
# NOTE : To know more about the Django url visit below URL 
#  URL : https://docs.djangoproject.com/en/1.11/topics/http/urls/
#
# -------- <<< STEP 4 - 6 dealing with the [POST] method >>> ----------
#
# STEP 4 :  Serializer (Creating Serializers)
# Serializer objects will help to describe the data from and return the data to our API. It basically converts the text string into JSON  format and viceversa. 
# Seralizers allows complex data types such as querysets and model instance to be converted into python datatypes which can be easily converted to JSON, XML or other content types. 
# Seralizer will also provide help to deserialize the parsed data into complex data types after validating the first incoming data types
#  
# For our API we will be creating a seralizer within our application base directory as 'serializers.py' and it will have below contents 
#
# | $
# | $ pwd
# | /opt/django_project/profile-rest-api/src/profiles_project/profiles_api
# | $ cat  serializers.py 
# | from rest_framework import serializers
# | 
# | class HelloSerializer(serializers.Serializer): 
# |     """ Serializes the name field for our APIView """
# | 
# |     name = serializers.CharField(max_lenth=10)
# | $ 
# | $
# | 
#
# STEP 5 : Adding serializers to the APIView and creating POST method
# Once we have created the serializer our next step is to update the 'views.py' with below details 
#
# 1. Update the 'status' module from the 'rest_framework' class
# 2. Import the 'serializers' module from the apps base directory 
# 3. Declare a object like serializer_class = serializers.HelloSerializer [ Need to find more details about it ]
# 4. Create a 'POST' method within the 'HelloApiView' class which handle the POST request to our API
# 5. Intialize a 'serializer' object within the class  which can carry the data comes in as part of tge post request
# 6. Create an if condition which can retrun the name variable posted if it is valid 
# 7. Create an else condition to retrun Error and HTTP status code if its not a valid variable 
#
# | $ cat  views.py 
# | from django.shortcuts import render
# | 
# | from rest_framework.views import APIView		# This imports the APIView class from the django rest_framework views 
# | from rest_framework.response import Response	# This will process output which we need to return in JSON format with status codes 
# | from rest_framework import status			# This will help to return a status code for for API
# | 
# | from . import serializers
# | 
# | # Create your views here.
# | 
# | class HelloApiView(APIView):
# |     """ Test API View """
# | 
# |     serializer_class = serializers.HelloSerializer
# |     
# |     def get(self, request, format=None):
# |         """ Returns a list of APIView Features """
# | 
# |         an_apiview = [
# |             'Uses HTTP methods as functions (get, post, patch, put , delete)',
# |             'It is similar to traditional Django view',
# |             'Gives you the most control over your application logic', 
# |             'Its manually mapped to URLs'
# |         ]
# | 
# |         family_details = {
# |             'Father'   : 'Ajayaghosh V L',
# |             'Mother'   : 'Aparna A',
# |             'Daughter' : 'Vaiga Shanti A',
# |             'Son'      : 'Rishi Krishna A',
# |         }
# | 
# | 
# |         # response has to be always send it a dictionary format, for that we will associate our list with a key as seen below 
# |         return Response({'Message' : 'Hello, welcome to Ajay\'s first api endpoint', 'an_apiview': an_apiview, 'family_details' : family_details })
# | 
# |   def post(self, request):
# |         """ This will return the same name which is getting pasted """
# | 
# |         """ Meaning of below is this will initialize the 'serializer' with HelloSerializer which we defined in the serializers.py in apps base dir
# |             Also the 'request' will contain all information while we make a post request, amongst that actual data can be fetched out using 'request.data' """
# |         serializer = serializers.HelloSerializer(data=request.data)
# | 
# |         if serializer.is_valid():
# |             name = serializer.data.get('name')
# |             message = 'Hello {0}'.format(name)
# |             return Response({'message': message})
# |         else:
# |             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# | $ 
# | $
# | 
#
# STEP 6 : Try to post a request and see the output 
# Login to a remote host and then try to post a request to HelloView API and see if that return the name as posted 
#
# | 
# | [root@sathsang sample_scripts]# cat test_post_hello_api.py 
# | #!/usr/bin/python
# | #
# | # Script to check the working status of hellp.api
# | #
# | 
# | from pprint import pprint
# | import requests 
# | 
# | #
# | main_url = 'http://rhceclient01.svr.apac.sathsang.net:8080/api/'
# | sub_url  = 'hello-view/'
# | #
# | def get_api_content(bae_api, api_key):
# |     
# |     full_url = bae_api + api_key
# |     connect = requests.post(full_url, {'name': 'Ajayaghosh'})
# |     pprint (connect.json())
# | 
# | get_api_content(main_url, sub_url)
# | 
# | [root@sathsang sample_scripts]# python test_post_hello_api.py 
# | {u'message': u'Hello Ajayaghosh'}
# | [root@sathsang sample_scripts]# 
# | 
#
# -------- <<< STEP 7 - 8 dealing with PUT, PATCH and DELETE methods >>> ----------
#
# STEP 7 : Define PUT, PATCH and DELETE methods 
# One you have define your GET and POST methods and its working then it is very easy to define the PUT, PATCH and DELETE methods 
# When you define these three methdods you will need to mention a 'key' which needs to get updated, in our sample file we have used 'pl' with the method
#
# | $
# | $  cat views.py 
# | from django.shortcuts import render
# | 
# | from rest_framework.views import APIView		# This imports the APIView class from the django rest_framework views 
# | from rest_framework.response import Response		# This will process output which we need to return in JSON format with status codes 
# | from rest_framework import status			# This will help to return a status code for for API
# | 
# | from . import serializers
# | 
# | # Create your views here.
# | 
# | class HelloApiView(APIView):
# |     """ Test API View """
# | 
# |     serializer_class = serializers.HelloSerializer
# |     
# |     def get(self, request, format=None):
# |         """ Returns a list of APIView Features """
# | 
# |         an_apiview = [
# |             'Uses HTTP methods as functions (get, post, patch, put , delete)',
# |             'It is similar to traditional Django view',
# |             'Gives you the most control over your application logic', 
# |             'Its manually mapped to URLs'
# |         ]
# | 
# |         family_details = {
# |             'Father'   : 'Ajayaghosh V L',
# |             'Mother'   : 'Aparna A',
# |             'Daughter' : 'Vaiga Shanti A',
# |             'Son'      : 'Rishi Krishna A',
# |         }
# | 
# | 
# |         # response has to be always send it a dictionary format, for that we will associate our list with a key as seen below 
# |         return Response({'Message' : 'Hello, welcome to Ajay\'s first api endpoint', 'an_apiview': an_apiview, 'family_details' : family_details })
# | 
# |     def post(self, request):
# |         """ This will return the same name which is getting pasted """
# | 
# |         """ Meaning of below is this will initialize the 'serializer' with HelloSerializer which we defined in the serializers.py in apps base dir
# |             Also the 'request' will contain all information while we make a post request, amongst that actual data can be fetched out using 'request.data' """
# |         serializer = serializers.HelloSerializer(data=request.data)
# | 
# |         if serializer.is_valid():
# |             name = serializer.data.get('name') # With this 'name' variable which declared within 'HelloSerializer' will assigned to name variable here 
# |             message = 'Hello {0}'.format(name) # Formatting technique in python 
# |             return Response({'message': message})
# |         else:
# |             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # This will retun error and HTTP status code using Response module
# | 
# |     def put(self, request, pk=None):                        # => PUT Method, here its only returns a message 
# |         """ This method will help to update an object """
# | 
# |         return Response({"message" : "You have used the put method"})
# | 
# |     def patch(self, request, pk=None):                      # => PATCH Method, here its only returns a message 
# |         """ This method will help to update few fields in the object """
# | 
# |         return Response({"message": "You have used the patch method"})
# | 
# |     def delete(self, request, pk=None):                     # => DELTE Method, here its only returns a message 
# |         """ This methhod will help to delete an object """
# | 
# |         return Response({"message" : "This method will delete an object"})
# | 
# |         (profile_rest_api) [root@rhceclient01 profiles_api]# 
# | $
# | $
#
# STEP 8 : Now login to another host and test the newly defined PUT, PATCH and DELETE methods 
#
# | [root@sathsang sample_scripts]# cat  test_post_hello_api.py 
# | #!/usr/bin/python
# | #
# | # Script to check the working status of hellp.api
# | #
# | 
# | import requests 
# | 
# | #
# | main_url = 'http://rhceclient01.svr.apac.sathsang.net:8080/api/'
# | sub_url  = 'hello-view/'
# | #
# | def put_api_content(bae_api, api_key):
# |     
# |     full_url = bae_api + api_key
# |     connect = requests.put(full_url, {'name': 'Ajayaghosh'})
# |     print 'Output from put method \n {0}'.format(connect.json())
# | 
# | def patch_api_content(bae_api, api_key):
# | 
# |     full_url = bae_api + api_key
# |     connect = requests.patch(full_url, {'name': 'Ajayaghosh'})
# |     print 'Output from patch method \n {0}'.format(connect.json())
# | 
# | def delete_api_content(bae_api, api_key):
# | 
# |     full_url = bae_api + api_key
# |     connect = requests.delete(full_url)
# |     print 'Output from delete method \n {0}'.format(connect.json())
# | 
# | 
# | put_api_content(main_url, sub_url)
# | patch_api_content(main_url, sub_url)
# | delete_api_content(main_url, sub_url)
# | 
# | [root@sathsang sample_scripts]# python test_post_hello_api.py 
# | Output from put method 
# |  {u'message': u'You have used the put method'}
# | Output from patch method 
# |  {u'message': u'You have used the patch method'}
# | Output from delete method 
# |  {u'message': u'This method will delete an object'}
# | [root@sathsang sample_scripts]# 
#
#
#-------------------------------------------------------------------------------------------------------------
# Chapter 4 : Django REST Framework Views - Viewsets
#-------------------------------------------------------------------------------------------------------------
# Similar to apiview, django provides another method of designing an API which is called viewset. 
# Viewset will also help to find the endpoint which is written in the fucntion. 
# 
# There are couple of adavanatges and use cases which makes us to use Viewset over APIView, few are 
#
# . Viewsets uses Model operations functions instead of the http methods Viewsets provoides some default object along with the APIs, few of the operations it provides are 
# - List           : For geting a list of objects 
# - Create         : Creating a new object 
# - Retrive        : Retrive a new object 
# - Update         : For updating an object
# - Partial Update : For updating part of an object 
# - Destroy        : To delete an object
#
# Along with this Viewsets will take care of standard logic for you 
# - They are perfect for running standard database operation 
# - They are the fatest way to interact with the database backend
# 
# * Example of using viewsets 
# Below are few examples or use cases we are given along with the viewsets 
# - In case we need a simple Create, Read, Update and Delete operation with the database. 
# - In case you want a quick and simple API to manage predefined object 
# - You need little or no custom logic to the embedded logic within Django 
# - In case you are working with a standard data structure 
# 
# * Creating a API ViewSet
# We will be going through a step by step procedure to create a viewset
# 
# STEP 1 : Creating Views under the apps views.py file 
# In our case we will be updating the views.py under or apps directory '/opt/django_project/profile-rest-api/src/profiles_project/profiles_api/views.py' 
# Additional to the classes we defined earlier to the APIview we will including one more class for viewset 
# 'from rest_framework import viewsets' , This will help us to get the viewset configured 
# 
# | $
# | $ vim /opt/django_project/profile-rest-api/src/profiles_project/profiles_api/views.py
# | from django.shortcuts import render
# | 
# | from rest_framework.views import APIView		# This imports the APIView class from the django rest_framework views 
# | from rest_framework.response import Response	# This will process output which we need to return in JSON format with status codes
# | from rest_framework import status		        # This will help to return a status code for for API
# | from rest_framework import viewsets                 # ** This module will take care of the Viewset operations **
# | 
# | from . import serializers
# | 
# | # Create your views here.
# | 
# | class HelloApiView(APIView):                        # ==> This is the carry over class already defined for APIView and not relevant for this session
# |     """ Test API View """
# | 
# |     serializer_class = serializers.HelloSerializer
# |     
# |     def get(self, request, format=None):
# |         """ Returns a list of APIView Features """
# | 
# |         an_apiview = [
# |             'Uses HTTP methods as functions (get, post, patch, put , delete)',
# |             'It is similar to traditional Django view',
# |             'Gives you the most control over your application logic', 
# |             'Its manually mapped to URLs'
# |         ]
# | 
# |         family_details = {
# |             'Father'   : 'Ajayaghosh V L',
# |             'Mother'   : 'Aparna A',
# |             'Daughter' : 'Vaiga Shanti A',
# |             'Son'      : 'Rishi Krishna A',
# |         }
# | 
# |         fstab_file = open('/etc/fstab', 'r')
# |         content = fstab_file.readlines()
# | 
# | 
# |         # response has to be always send it a dictionary format, for that we will associate our list with a key as seen below 
# |         #return Response({'Message' : 'Hello, welcome to Ajay\'s first api endpoint', 'an_apiview': an_apiview, 'family_details' : family_details , 'fstab' : content})
# |         return Response({'fstab contents' : content})
# | 
# |     def post(self, request):
# |         """ This will return the same name which is getting pasted """
# | 
# |         """ Meaning of below is this will initialize the 'serializer' with HelloSerializer which we defined in the serializers.py in apps base dir
# |             Also the 'request' will contain all information while we make a post request, amongst that actual data can be fetched out using 'request.data' """
# |         serializer = serializers.HelloSerializer(data=request.data)
# | 
# |         if serializer.is_valid():
# |             name = serializer.data.get('name') # With this 'name' variable which declared within 'HelloSerializer' will assigned to name variable here 
# |             message = 'Hello {0}'.format(name) # Formatting technique in python 
# |             return Response({'message': message})
# |         else:
# |             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # This will retun error and HTTP status code using Response module
# | 
# |     def put(self, request, pk=None):
# |         """ This method will help to update an object """
# | 
# |         return Response({"message" : "You have used the put method"})
# | 
# |     def patch(self, request, pk=None):
# |         """ This method will help to update few fields in the object """
# | 
# |         return Response({"message": "You have used the patch method"})
# | 
# |     def delete(self, request, pk=None):
# |         """ This methhod will help to delete an object """
# | 
# |         return Response({"message" : "This method will delete an object"})
# | 
# |         
# | 
# | class HellowViewSet(viewsets.ViewSet):                      ==> Creating View set for our requirement
# |     """Test Hello Viewset"""
# | 
# |     def list (self, request):
# |         """Return a Hello Message"""
# |         a_viewset = [
# |             "Uses actions (list, create, retrieve, update, partial_update",
# |             "Automatically maps URLs using routers",
# |             "Provide more functionality with less code",
# |         ]
# | 
# |         return Response({'message' : 'This is a viewset', 'a_viewset': a_viewset})
# |
# | $ 
#
# STEP 2 : Configure using URL routers
# Using routers you can easily map your class to the API urls. This is an important feature provided for ViewSets.
# To do this what you need to do is, you will need to navigate to the apps dirctory and open the urls.py file 
#
# NOTE : You will need to update the application url.py file not the project file 
#
# Below is the sample configuration for urls.py 
#
# | root@rhceclient01 profiles_api]# 
# | [root@rhceclient01 profiles_api]# cat /opt/django_project/profile-rest-api/src/profiles_project/profiles_api/urls.py 
# | from django.conf.urls import url	                # This module is to handle the url
# | from django.conf.urls import include                # Using for including the router.urls for ViewSet
# | from rest_framework.routers import DefaultRouter    # Importing the DefaultRouter class to handle urls for ViewSet
# | 
# | from . import views			        # We are importing views.py in our apps base directory here
# | 
# | # Creating a router object from DefaultRouter class and mapping 'views.HellowViewSet' class with base name 'hello-viewset'
# | router = DefaultRouter()
# | router.register('hello-viewset', views.HellowViewSet, base_name='hello-viewset')
# | 
# | urlpatterns = [ 
# |     
# |     # Using the url module, we are defining the api view 'hello-view/'
# |     # hello-view will display the get method defined under the HelloApiView class under the 'views.py' as the view
# |     url(r'^hello-view/', views.HelloApiView.as_view()),
# | 
# |     # Here we are making the advntage of include module and DefaultRouter class
# |     # Using this urls will automatically mapped according to how they are associated to objects
# |     url(r'', include(router.urls))
# |     ]
# | 
# | 
# | [root@rhceclient01 profiles_api]# 
# | [root@rhceclient01 profiles_api]# 
# | 
#
# STEP 3 : Once this done verify the Django server is running fine without any error and test the api
# Once verified the django server is running successfully, query the site as below 
#
# | >>> from pprint import pprint 
# | >>> import requests
# | >>> connect = requests.get('http://djangorestapi01.svr.apac.sathsang.net:8080/api/hello-viewset/')
# | >>> print(connect.status_code)
# | 200
# | >>> pprint(connect.json())
# | {u'a_viewset': [u'Uses actions (list, create, retrieve, update, partial_update',
# |                 u'Automatically maps URLs using routers',
# |                 u'Provide more functionality with less code'],
# |  u'message': u'This is a viewset'}
# | >>> 

