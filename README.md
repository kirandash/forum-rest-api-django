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

### 3.16 Uploading and Handling images
1. For handling image: better option: use Django Storage ---> which uses AWS S3
2. Add media details in settings.py - Add MEDIA_ROOT and MEDIA_URL
3. Test image upload from rest_framework_api.py with do_img fn
4. Note: Issue right now is: put isn't updating the same id but creating a new post.
5. Fix put issue:
    - unable to receive id and thus making a post instead of put. fetch proper id in put method

### 3.17 Roll back Views for CRUDL - two endpoints
1. Although we could handle all CRUDL operations with one endpoint. It became complicated. Thus, better not to use one endpoint for all methods. Refactor the code to separate the mixins to different endpoints.
2. status/api/views.py
    - Roll back to having two classes to have two endpoints
3. Test at: 
    - http://localhost:8000/api/status/
    - http://localhost:8000/api/status/7/

### 3.18 Authentication & Permissions
1. Right now, we need to send user info in request body to make CRUD operation. user info should be taken based on session. Also right now our endpoints are public. We should enable authentication now.
2. status/api/views.py
    - Add authentication class SessionAuthentication to StatusAPIView
    - Add permission class IsAuthenticated to StatusAPIView (IsAuthenticated will ask auth for all CRUD operation)
    - IsAuthenticatedorReadonly will check for auth, if not available, will return readonly fields. Ex: GET call will work.
3. status/api/serializers.py
    - Make user field read only. So that it can't be edited from POST etc.
    - Docs: read_only_fields https://www.django-rest-framework.org/api-guide/serializers/#specifying-read-only-fields
4. Test http://localhost:8000/api/status/
    - if not authenticated only GET will be accessible
    - if authenticated, will be able to see POST method
5. Bug fix: views.py: perform_create should be added to be able to create new posts.

### 3.19 Global settings for Authentication and Permission in settings.py file
1. Since all of the API classes are going to have common settings. we will define all the rest configuration in forum/restconf/main.py file.
2. Import main.py in settings.py file
3. Docs: 
    - authentication settings: https://www.django-rest-framework.org/api-guide/authentication/#setting-the-authentication-scheme
    - permission settings: https://www.django-rest-framework.org/api-guide/permissions/
4. Now we can comment our settings in StatusAPIView and StatusDetailAPIView. So, it will use settings from settings.py file ---> restconf ---> main.py file
5. Global settings of settings.py file can be overwritten in individual views.

### 3.20 Permission Tests with Python requests
1. scripts/rest_framework_api.py
    - Add script
    - Run script using python
2. Note: 
    - JWT auth is best if all endpoints are for internal authentication. viz(React, Angular auth etc) Ex: Netflix uses JWT and not auth. As their APIs are not exposed to 3rd party.
    - Oauth or Oauth2 is recommended if we have to authenticate 3rd party services viz twitter etc to access our DB

### 3.21 Implement JWT Authentication
1. Docs: REST framework JWT Auth: https://jpadilla.github.io/django-rest-framework-jwt/
2. JWT (JSON Web Token)
3. Follow installation instructions from doc
    - `pip install djangorestframework-jwt`
    - Add `JSONWebTokenAuthentication` to REST_FRAMEWORK settings in main.py
    - Add path to forum/urls.py
    - Test at: http://localhost:8000/api/auth/jwt/. Pass username and pwd and it will return a token.
4. Test with python request:
    - forum_projects/scripts/rest_framework_api.py
5. Implement **refresh token** feature. If JWT_ALLOW_REFRESH is True, non-expired tokens can be "refreshed" to obtain a brand new token with renewed expiration time.
6. Add test to forum_projects/scripts/rest_framework_api.py
7. Add settings for JWT_AUTH in main.py and set JWT_ALLOW_REFRESH as True
8. Run test with python rest_framework_api.py

### 3.22 JWT Authorization header
1. Send `"Authorization": "JWT " + token,` in headers to API calls.
2. Note: The prefix JWT can be changed in main.py file: JWT_AUTH_HEADER_PREFIX
3. Note: JWT from DRF auto adds content type as json. No need to force, especially with file types being sent.

### 3.23 Custom JWT response payload handler - add username, expires info
1. We will modify payload of response.
    - JWT_RESPONSE_PAYLOAD_HANDLER
    - Responsible for controlling the response data returned after login or refresh. Override to return a custom response such as including the serialized representation of the User.
    - Defaults to return the JWT token.
2. Create new app: `python manage.py startapp accounts`
    - Add to settings.py file
    - `python manage.py makemigrations`
    - `python manage.py migrate`
3. Create accounts/api/
    - __init__.py file
    - utils.py file
4. overwrite jwt_response_payload_handler in utils.py file
5. Add utils.py file to main.py - JWT_RESPONSE_PAYLOAD_HANDLER
6. Now posting username and password to http://localhost:8000/api/auth/jwt/ will return token and username.
7. Add expiration detail from JWT_REFRESH_EXPIRATION_DELTA and add to payload so that we can show a warning to user that session is about to expire and refresh the token.

### 3.24 Custom authentication view
1. Currently, we are able to get the token from api/auth/jwt endpoint. We will customize it to get the token in multiple ways.
2. Docs: - https://jpadilla.github.io/django-rest-framework-jwt/ - Read section "Creating a new token manually"
3. Create accounts/api/
    - urls.py file, 
    - views.py file 
4. Move jwt related urls to api/urls.py file
5. Create AuthView in api/views.py file
6. Test from scripts/rest_framework_api.py file

### 3.25 Test auth view for email and already authenticated
1. scripts/rest_framework_api.py - add test script
2. add email to user and test

### 3.26 Register API view
1. Create a new view to register users as well
2. Add RegisterAPIView to accounts/api/views.py file
3. Add views to urls.py file
4. Test rest_framework_api.py 

### 3.27 User Register Serializer
1. Right now the RegisterAPIView doesn't use serializer and we manually have to mention all the fields. We are going to change that by adding a serializer to handle the fields for RegisterAPIView in a better way. 
2. Create accounts/api/serializers.py file
    - Create UserRegisterSerializer
3. Use UserRegisterSerializer in accounts/api/views.py file
4. Run test script for registration

### 3.28 Serializer method field
1. accounts/api/serializers.py
    - Create serializer method field for token, expires
    - Create alternate serializer method to use token_response

### 3.29 Get Context data
1. Pass request data to serializer from view using get_serializer_context method

### 3.30 Refactoring UserRegisterSerializer
1. Remove get_token_response as we are already handling token and expires
2. Add success message
3. Make user's not active by default. (should be activated after email verification - not implemented)
4. Run test script - check success message in terminal and check user status in admin: http://localhost:8000/admin/auth/user/15/change/

### 3.31 Custom Permissions for views
1. Django by default has permissions ex: AllowAny, AllowAll, AuthenticatedOnly. We will create custom permissions for BlacklistPermission, IsOwnerOrReadOnly, AnonPermissionOnly
2. Docs: Permissions examples:
    - https://www.django-rest-framework.org/api-guide/permissions/#examples
3. Create accounts/api/permissions.py
    - copy BlacklistPermission, IsOwnerOrReadOnly example from doc.
    - Create AnonPermissionOnly for non authenticated users only
4. views.py
    - Add AnonPermissionOnly to RegisterAPIView, AuthAPIView. Since the API should be for anonymous users only. Not for all.
5. Test accessing register endpoint with existing token.

### 3.32 Is owner or read only permission
1. Add is owner permission check to StatusDetailAPIView. as we want only the owner to be able to perform put/patch/delete operation on their status.
2. modify status/models.py - to create owner property and status/api/views.py - to import permission
3. Test: python rest_framework_api.py. Check that user can't modify other user's posts.

Note: Concepts above are enough to create a fully functional APIs. All new concepts are for improving the API.

### 3.33 Nested Serializer - for user and add uri info
1. Right now the status detail api endpoint returns only user id. We will customize it to add more info like: username etc.
2. accounts/api/serializers.py
    - Create UserPublicSerializer to show users publicly with username
3. status/api/serializers.py
    - Add UserPublicSerializer to StatusSerializer's user field.
4. Run test and now: detail view should return username and user id in a nested JSON structure.
5. Also add uri information for user and status serializers. Better coding practice so in future other developers can locate the endpoint for serialized fields easily.
6. Test if uri is added at: 
    - http://localhost:8000/api/status/12/
    - http://localhost:8000/api/status/

### 3.34 Nested Serializer - for query sets of status lists in user endpoint
1. Create api/user/views.py - UserDetailAPIView
2. Create api/user/serializers.py - UserDetailSerializer
3. Create api/user/urls.py file. Include in forum/urls.py file
4. Test endpoint at: http://localhost:8000/api/user/kiran/
    - should include user info + status 

### 3.35 Nested Serializer - user detail - status endpoint
1. Create UserStatusAPIView. Add view to urls.py
2. Test at: http://localhost:8000/api/user/kiran/status/ 
3. Include status_uri to UserDetailSerializer
4. Restructure detail user serializer for status. Add last status, recent status list to endpoint data
5. Test at: http://localhost:8000/api/user/kiran/
6. Also add limit to UserDetailSerializer
7. Test at: http://localhost:8000/api/user/kiran/?limit=3 - should return 3 recent posts

### 3.36 DRF Pagination to manage request load
1. accounts/api/user/views.py
    - UserStatusAPIView - add pagination_class (Create restconf/pagination.py file, include default pagination settings in main.py file)
2. Test pagination at http://localhost:8000/api/user/kiran/status/ - should show multiple pages with each page having only 5 status
3. Can go to next page with: http://localhost:8000/api/user/kiran/status/?page=2
4. Docs: https://www.django-rest-framework.org/api-guide/pagination/
5. Note: LimitOffsetPagination - for settings limit and offset. PageNumberPagination only shows limit but not offset.
6. Limit offset test at: http://localhost:8000/api/user/kiran/status/?limit=2&offset=6

### 3.37 Search Filter & Ordering using DRF
1. Add settings in main.py file
2. Add search_fields (username, content) to StatusAPIView
3. Test at: http://localhost:8000/api/status/ - new filter button should be available.
4. Search query: http://localhost:8000/api/status/?search=kiran -- search username and content
5. can remove the get queryset filter implemented earlier with q.
6. Filter with ordering: http://localhost:8000/api/status/?ordering=-timestamp&search=kiran
7. Add search and ordering filter to user status view:
    - http://localhost:8000/api/user/kiran/status/?search=ttt

### 3.38 Reverse URLs with DRF to create full URIs in endpoints
1. accounts/api/user/serializers.py:
    - Modify get_uri fn to return accurate urls using DRF reverse in UserDetailSerializer.
2. forum/urls.py: 
    - Add namespace to status and users endpoint
3. Make sure app_name is given for respective namespaces in user/urls.py, status/api/urls.py
4. Test at: http://localhost:8000/api/user/kiran/
5. Add the same for status/api/serializers.py
6. Test at: http://localhost:8000/api/status/

### 3.39 Serializer Related Fields
1. Docs: Serializer Relations: https://www.django-rest-framework.org/api-guide/relations/#serializer-relations
2. Relational fields are used to represent model relationships. They can be applied to ForeignKey, 
ManyToManyField and OneToOneField relationships, as well as to reverse relationships, and custom relationships 
such as GenericForeignKey.
3. For endpoint: http://localhost:8000/api/status/
    - Add user_id, user_link, username in StatusSerializer
    - Note: user obj is directly accessible to Status model here
4. Accessing indirect models eg: UserDetailSerializer using a related name (source set)
    - access statuses
    - Test at: http://localhost:8000/api/user/kiran/

### 3.40 Automated Testing
1. Docs:
    - Django: https://docs.djangoproject.com/en/3.0/topics/testing/overview/
    - DRF: https://www.django-rest-framework.org/api-guide/testing/#testing
2. accounts/tests.py:
    - Create test case: test_created_user
3. status/tests.py:
    - Create test case: 
4. Run test: `python manage.py test`
5. Note: 
    - pre-requisites for all tests should be written in setUp fn.
    - test fns should start with `test_`

### 3.41 Testing User API
1. Will test user creation using API endpoint and not just the Django model.
2. accounts/api/test_user_api.py file
    - Note: file name should start test viz test_user_api.py or called tests.py.
    - Add test cases for : test_creating_user, test_register_user_api_fail, test_register_user_api, test_login_user_api
3. forum/urls.py and api/urls.py - Make sure namespace and url names are added
4. DRF Status codes: https://www.django-rest-framework.org/api-guide/status-codes/

### 3.42 Testing status API
1. status/api/tests.py file
    - Add test cases

### 3.43 Testing with Temporary Image
1. status/api/tests.py file
    - Add test cases

### 3.44 More concepts
1. Throttling: 
    - limiting no of requests a client can make
    - https://www.django-rest-framework.org/api-guide/throttling/
    - Best to implement for 3rd party APIs
2. ViewSets:
    - https://www.django-rest-framework.org/api-guide/viewsets/
    - Try to avoid ViewSets if possible. It adds extra complexity to simpler concept
    - Better to use Generic Viewsets like we did above - raw and simple to use
3. Parsers:
    - https://www.django-rest-framework.org/api-guide/parsers/
    - The default JSON parser is good enough. But can use DRF parser if reqd
