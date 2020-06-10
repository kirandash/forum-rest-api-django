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
6. Note: For production projects: always better to choose LTS version which is 2.2 right now for Django. Check LTS version at: https://www.djangoproject.com/download/

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

## 3. Creating API with djangorestframework
### 3.1 Install Django Rest Framework
1. Go to https://www.django-rest-framework.org/ and check for requirements.
2. Install drf: follow installation guides
    - From venv: `pip install djangorestframework`
    - `pip install markdown` gives Markdown support for the browsable API.
    - `pip install django-filter` gives Filtering support
3. Note: after every new installation - save your requirements file with: `pip freeze > requirements.txt`
4. Add 'rest_framework' to INSTALLED_APPS

### 3.2 Create status app, Add model, manager
1. Create app: `python manage.py startapp status`
2. Add status to settings.py file
3. Create Status model in status/models.py file
4. makemigrations and migrate
5. Register model to admin

### 3.3 Overwrite default admin form with ModelForm for validations
1. status/models.py
    - Add singular and plural labels/verbose_name
2. In admin: create a status post. And you will see that, only user is mandatory. To make content and image also mandatory we will add form validations. (using django forms) Also we will add number of character validations.
3. Create status/forms.py file.
    - Add StatusForm class from forms.ModelForm to create form validation.
4. status/admin.py
    - add StatusForm to admin
5. Test list display at: http://localhost:8000/admin/status/status/
6. Create a new status to check validation. Form should not submit with blank content & image. At lease one has to be provided.
7. We have implemented simple validations. But the same approach can be used to create complex, custom validations for model fields that Django does not provide out of the box.

### 3.4 Creating a Serializer
1. To exchange data b/w Django and External env viz: React/Angular/any device: we will use JSON(JavaScript Object Notation) format.
2. Serializers by DRF. Purpose:
    - serializers are used to convert Python data into JSON format which can then be served via API endpoints.
    - serializers can also be used to validate data
    - serializers can be used to create / update data. No need of serializer for delete. The entire obj can be directly deleted with obj.delete method.
3. Create status/api/serializers.py file
    - Create StatusSerializer class
4. Tips on **accessing/working with JSON data** from shell:
    - From venv: `python manage.py shell`
    - `import json` json library from python
    - `data = {'abc':123}` create a python dict
    - `data_list = ['abc']` create a data list
    - `data_json = json.dumps(data)` converts python dict to a json string
    - `data_json` return json string
    - `load_json = json.loads(data_json)` loads json data as list
    - `load_json['abc']`
5. Tips on serializing data from Shell:
    - **Serializing an Object**: 
        - From venv: `from status.models import Status`
        - `from status.api.serializers import StatusSerializer`
        - `obj = Status.objects.first()`
        - `obj`
        - `data = StatusSerializer(obj)`
        - `data`
        - `data.data` serialized data (not json yet)
        - test if json or not by `json.loads(data.data)`: throws error, since not json
        - `from rest_framework.renderers import JSONRenderer`
        - `new_json_data = JSONRenderer().render(data.data)`
        - `new_json_data` shows bytes data in JSON
        - `json.loads(new_json_data)` returns JSON data
    - **Serializing a query set**
        - `qs = Status.objects.all()`
        - `serializer = StatusSerializer(qs,many=True)`
        - `serializer.data`: returns an ordered dictionary
        - `json_data = JSONRenderer().render(serializer.data)`
        - `json_data` shows bytes data in JSON
        - `import json`
        - `json.loads(json_data)` returns JSON data

### 3.5 Creating a Serializer - Create/Update/Delete object from shell
1. Crate object from shell using serializer: `is_valid() and save()`
    - From venv: `python manage.py shell`
    - `from status.models import Status`
    - `from status.api.serializers import StatusSerializer`
    - `data={'user':1}`
    - `serializer = StatusSerializer(data=data)`
    - `serializer.is_valid()` returns T/F
    - `serializer.save()` Note: must run is_valid before save(). Saves the data after serializing
    - `Status.objects.count()`
    - `Status.objects.all()` check if new obj is created
2. Update object from shell using serializer: `is_valid() and save()`
    - `obj = Status.objects.first()`  # grab the obj to update
    - `data = {'content': 'some new content'}`  # data to update
    - `update_serializer = StatusSerializer(obj, data=data)`
    - `update_serializer.is_valid()`: returns False
    - **Check errors** by `update_serializer.errors`
    - `data = {'content': 'some new content', 'user': 1}`
    - `update_serializer = StatusSerializer(obj, data=data)`
    - `update_serializer.is_valid()`: returns True
    - `update_serializer.save()`
3. Delete object from shell using model object: `obj.delete()`
    - `data = {'user': 1, 'content': 'Please delete me'}`
    - `create_obj_serializer = StatusSerializer(data=data)`
    - `create_obj_serializer.is_valid()`
    - `create_obj = create_obj_serializer.save()`
    - `print(create_obj)`
    - `print(create_obj.id)`
    - `obj = Status.objects.last()`  # grab the recent obj to delete
    - `get_data_serializer = StatusSerializer(obj)`
    - `print(get_data_serializer.data)`
    - `print(obj.delete())`  # delete the object. No need of serializer to delete
    - Note: To delete an object, we don't need serialize. Serializer is helpful when we try to create or update data, because we have to mention the fields. But while deleting just deleting the entire obj will do the job. We don't need field level details.

### 3.6 Validations with ModelSerializer, CustomSerializer for plain fields
1. can validate a serializer field with `validate_fieldname` fn - Field level validation
2. Add validate_content to status/serializers.py file
3. Note: the validation is equivalent to validations added earlier in forms.py file.
4. Add validate method to StatusSerializer to validate all content types. - model level validation

### 3.7 API Endpoint - Create urlpatterns
1. Create status/api/urls.py and views.py files.
2. Add urlpatterns for all views
3. Docs:
    - https://docs.djangoproject.com/en/3.0/topics/http/urls/

### 3.8 List and Search API View with APIView, generics.ListAPIView
1. status/api/views.py
    - Create StatusListSearchAPIView from rest_framework: APIView
2. Include status/api/urls.py in main project forum/urls.py file
3. Test at: http://localhost:8000/api/status/
    - Only GET allowed
4. status/api/views.py
    - Create StatusAPIView with generics.ListAPIView, better way of handling get calls
    - Can overwrite the default qs using get_queryset method
    - Test at: /api/status/?q=delete - will return all status with content that has text delete
    - /api/status/ - will return all status without any filter

### 3.9 Create API View with generics.CreateAPIView
1. status/api/view.py:
    - Create StatusCreateAPIView
2. Add StatusCreateAPIView to status/api/urls.py file
3. Test at: http://localhost:8000/api/status/create/
    - Get not allowed. Only post

### 3.10 Detail API View with generics.RetrieveAPIView
1. status/api/views.py
    - Create RetrieveAPIView
    - To map id from urlpattern with view, there are 3 ways:
        - use 'pk' in url. It will map to view automatically
        - use lookupfield if not using 'pk' in url
        - overwrite get_object method and filter using kwargs
2. Test at: http://localhost:8000/api/status/8/

### 3.11 Update & Delete with generics.UpdateAPIView, DestroyAPIView
1. status/api/views.py
    - Create UpdateAPIView
    - Test at: http://localhost:8000/api/status/8/update/
    - Create DestroyAPIView
    - Test at: http://localhost:8000/api/status/8/delete/
2. Note: with generic api views, List, Retrieve, Update and Destroy views are to be created separately.
    - Better choice if we need only one of the CRUD operation
    - Not recommended if all CRUD operations are desired

### 3.12 Mixins to power http methods
1. Docs:
    - https://www.django-rest-framework.org/api-guide/generic-views/#mixins
2. status/api/views.py
    - Add CreateModelMixin to StatusAPIView
    - Docs: https://www.django-rest-framework.org/api-guide/generic-views/#createmodelmixin
    - Test http://localhost:8000/api/status/
        - Should have both GET and POST allowed on it now. Earlier only GET was allowed.
3. status/api/urls.py
    - Remove StatusCreateAPIView
4. status/api/view.py
    - Add UpdateModelMixin to StatusDetailAPIView
    - Docs: https://www.django-rest-framework.org/api-guide/generic-views/#updatemodelmixin
    - Add DestroyModelMixin to StatusDetailAPIView
    - Docs: https://www.django-rest-framework.org/api-guide/generic-views/#destroymodelmixin
    - Test all methods at: http://localhost:8000/api/status/5/
5. Remove StatusUpdateAPIView and StatusDeleteAPIView from api/urls.py file

### 3.13 RetrieveUpdateDestroyAPIView
1. Docs: https://www.django-rest-framework.org/api-guide/generic-views/#retrieveupdatedestroyapiview
2. status/api/views.py
    - Instead of adding mixins: we can just create another class using RetrieveUpdateDestroyAPIView

### 3.14 One API endpoint for CRUDL with DRF Mixins and ListAPIView
1. Will create one endpoint for all CRUD steps.
2. status/api/views.py
    - Test list view: http://localhost:8000/api/status/
    - Test detail view: http://localhost:8000/api/status/?id=6
    - Test query at: http://localhost:8000/api/status/?q=eat
3. status/api/urls.py
    - comment all views but StatusAPIView

### 3.15 One API endpoint for CRUDL with DRF Mixins and ListAPIView
1. To test rest apis:
    - from venv: `pip install requests`: package to create requests
    - Create forum_project/scripts/rest_framework_api.py file
    - Run script with `python rest_framework_api.py` command
2. Modify status/api/views.py to handle id request in get, put, patch, delete
