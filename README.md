# REST API with Python, Django and Django Rest Framework
## 1. API Basics
### 1.1 Understanding API
1. **API**: stands for Application Programming Interface
  - **Definition**: An API can be defined as method of communication between software components.
  - Ex: When you sign up or login on any website viz stackoverflow using your google or facebook account, you are basically using an API from google or facebook. So the API helps stackoverflow to communicate with google with the help of API.
  - Ex: Payment transaction on Stripe. Amazon uses an API to communicate with Stripe and then Stripe uses an API to communicate with specific bank.
  - Note: API is not always limited to communication b/w websites or applications. The communication b/w application and hardware devices also happen through API.
  - Ex: Whenever I make a video call using WhatsApp/Facebook, it interacts with my phone's camera through an API.
  - Ex: Sending signals to a robot using a software
  - Ex: Sharing your location using google maps. Google maps interact with your device through an API to get it's location.
2. **Types of API**:
  1. **Internal API**: Internal APIs basically communicate on local level. Ex: WhatsApp/Facebook uses an API to interact with my phone's camera on a local level.
  2. **External API**: External APIs are APIs that communicate with software or services from a third party. For example: authentication on stackoverflow using google or facebook. Here the authentication API is an external API for stackoverflow.

### 1.2 Understanding REST API
1. **REST API**
  - REST stands for: Representational State Transfer
  - **Definition**: Methods of communication between web components.
  - Or: REST API helps us to access, process and handle web resources.

## 2. Creating an API with only Django
### 2.1 Intro to Django
1. Most popular Python framework as of 2020. And 6th most popular overall. First release in 2005. Older than 14 years. Thus, will stay live for a long time.
    - https://hotframeworks.com
2. Can create an entire application using Django. Both Backend and Frontend.
3. Very easy to use as Django comes with many default features. Thus, Django is mostly preferred for applications with tighter deadlines. 
4. **Cons**: 
    - Not a minimal framework like Flask. As it comes with many built in features. So with Django, our project might have features that we don't even need.
    - lesser control over the functionality. Since many features are built in. It will behave as per Django providing lesser control to us.
5. In this app, we will use Django only for backend and React for frontend.

### 2.2 Explore 3 ways to Install Python
1. Only Python: https://www.python.org/downloads/. In our case: we will download this one. Let's see 2 more options:
2. Python distribution: A distribution is a version of Python that also comes pre-packaged with additional useful libraries
3. Distributions:
    - **Anaconda**: https://www.anaconda.com/products/individual
    - **Miniconda**: https://docs.conda.io/en/latest/miniconda.html : a smaller version of Anaconda without the additional packages
4. check version of installed python: `python --version` will return 2.7.16
    - `python3 --version`: will return 3.8.3
5. For Linting and debugging: Add Python extension by Microsoft in VSCode
6. Check path of installation: `which python` & `which python3`

### 2.3 Python package manager pip
1. In python to add any additional package we will use the package manager pip. It stands for pip installs package.
2. pip comes by default with python.
3. To install a package run: `pip install packagename`

### 2.4 Installing Virtual Environment
1. **Virtual Environment**: By default if we install any package it will install globally on our system. For example we want django in our project. To install django we need to run `pip install django`. But if I run that, it will install django on my system. But we don't want that. Since I can have multiple projects on my system and each project might need different version of django and different set of packages. Thus, We want to create a virtual python environment for our project. So that all the package requirements of our project will be installed in that virtual environment and not effect our global/system environment.
    - And once our project is finished, if we want the same project to run on a different machine, we don't need to send entire virtual environment to the new machine. All we have to do is create one file called requirements.txt which will hold list of all the packages. And use that file to install all packages for another virtual environment on a new system.
2. **Create venv** using: `python3 -m venv forum_venv`: -m stands for make
3. **activate**: `. forum_venv/bin/activate` or `source forum_venv/bin/activate`. Once activated: terminal prompt will start with (forum_venv)
4. **Deactivate**: `deactivate`

### 2.5 Install Django and djangorestframework
1. From venv: `pip install django` - installs django (latest: 3.0.6) and pytz library for timezone support
2. `pip install djangorestframework`. and add `rest_framework` to settings.py file.
3. Optional: If getting any warning, also upgrade pip `pip install --upgrade pip`.

### 2.6 Create Project
1. from venv: `django-admin startproject forum` or `django-admin startproject forum .` if you want it to be created in current directory
2. Rename main folder to `forum_project` to avoid confusion with inside project folder with same name.
3. manage.py: has all the code for running scripts
4. Run server: `cd forum_project` and `python manage.py runserver` no need to mention python3 again. Since venv was created with python3. we can directly use python.

### 2.7 PyCharm
1. Launch project with pycharm. Select folder that contains both venv and project. It automatically activates venv. unlike vscode where we have to manually activate.
2. Launch terminal and run `python manage.py runserver`
3. Instead of doing that again and again, we can configure PyCharm to do that for us.
    - Add Configuration ---> Add script path to manage.py, working directory path and parameters: runserver.
    - Click on Create configuration - apply and save
    - Click on green play icon to run server

### 2.8 Create new App, run migrations
1. The project folder forum_project is basically a container for all the apps that we can have on our website. Each module can be specified as an app which will perform a specific task.
2. Create app: `python manage.py startapp updates` or `django-admin startapp updates`
3. Add updates to list of INSTALLED_APPS
4. create migrations: `python manage.py makemigrations`
5. Apply migrations: `python manage.py migrate`
6. check migration: `python manage.py showmigrations`

### 2.9 create superuser
1. `python manage.py createsuperuser` - kiran, django1234

### 2.10 Create Models
1. updates/models.py
    - Create Update class
2. For handling image with models.ImageField, we need pillow library: from venv: `pip install pillow`
2. Register models to admin with `admin.site.register()`
3. `python manage.py makemigrations` and `python manage.py migrate`
4. Run or `python manage.py runserver`
5. Check at http://127.0.0.1:8000/admin/ or http://localhost:8000/admin/ - should show Updates under admin

### 2.11 Send JSON response with JsonResponse from django.http 
**Theory**
1. Once we have created a model, now we can create views. In default Django: under view, we normally render an HTML file. In our case since we are going to create an API we will return a response in JSON/XML format. Since JSON is a far better and popular approach, we will use JSON format for our response data.
    - JSON format also is far more easy to work with frontend frameworks viz react or angular. Since JSON is easily handled with JS. As JSON itself is JavaScript Object Notation.
    
**Code**
1. updates/views.py
    - create function based view: json_dummy_view and user JsonResponse to convert python dict to JSON dict.
2. updates/urls.py:
    - map endpoint to fn view.
3. Test on browser:
    - http://localhost:8000/dummy/
    - Install chrome extension JSONView to format JSON.

### 2.12 Sending JSON data with HttpResponse and json library - alternate to JsonResponse
1. updates/views.py
    - use json library from python to convert python dict into JSON dict
    - use HttpResponse to send the response back

### 2.13 Create a Class based View - for JSON endpoint
1. updates/views.py:
    - Create JsonDummyCBV
    - use django.views.generic ---> View: and return json response from get method
2. updates/urls.py:
    - map JsonDummyCBV.as_view() in url endpoint
3. Test on browser at: http://localhost:8000/dummy/cbv/

### 2.14 Mixins with CBVs
1. Mixin: A mixin is used to hold the common code among classes. Ex: We will hold the common code to send JSON response.
2. Create forum/mixins.py:
    - Create JsonResponseMixin to have to common code to send JSON response
3. updates/views.py:
    - Use mixin with JsonDummyCBVWithMixin
4. Test on browser at: http://localhost:8000/dummy/mixin/

### 2.15 Serialize Data with django.core.serializers
1. Serializing data: Converting data from one structure to another is called serializing data.
2. updates/views.py
    - 
3. Run **Fixture** to see serialized data of application:
    - `python manage.py dumpdata --format json --indent 4` : returns all data of our app
    - `python manage.py dumpdata updates.update --format json --indent 4` : returns data from updates app update model only. (Make sure to add few update items in admin)
4. Test on browser at: 
    - http://localhost:8000/dummy/serializer/detail/, 
    - http://localhost:8000/dummy/serializer/list/ - check with all fields and specific fields

### 2.16 Managers and Methods to serialize data in model instead of view
1. Move the serializing code from view to a callable method in models.py file.
    - updates/models.py: 
        - serialize entire model, serialize a single model instance
2. Cleaner view + Code re-usability

### 2.17 Change serialize manager and method for better JSON structure
1. updates/models.py
    - convert serialized data into structured data and return everything from under fields
2. Test both list and detail endpoint

### 2.18 Serialize List with The Dot values method and refactor detail view
1. Refactor JSON structure in updates/models.py using dot values method on a queryset
    - use self.values to get all the values and then dump into json
2. Test at: http://localhost:8000/dummy/serializer/list/
3. Refactor detail serializer as well in models.py file by not using any structure and directly mapping fields to JSON structure.
4. Test at: http://localhost:8000/dummy/serializer/detail/
