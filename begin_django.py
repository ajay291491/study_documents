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
# | $ vim /tmp/test
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
#
#
#
#
