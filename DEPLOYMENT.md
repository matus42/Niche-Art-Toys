# Deployment

Welcome to the deployment guide for my project. This guide includes detailed steps and instructions needed to deploy the application successfully on Heroku, using ElephantSQL for the database and AWS S3 for static and media file storage.

## **Table of Contents**

* [**Create Repository**](#create-repository)
* [**Setting up the Workspace**](#setting-up-the-workspace)
* [**Creating ElephantSQL Database**](#creating-elephantsql-database)
* [**Creating Heroku App**](#creating-heroku-app)
* [**AWS S3 Bucket**](#aws-s3-bucket)
* [**Environmental Variables**](#environmental-variables)
* [**settings.py File**](#settingspy-file)
* [**Cloning and Forking**](#cloning-and-forking)

## Create Repository
To deploy the site to Heroku, follow these steps to initialize your repository:

* Create a new GitHub repository and clone it to your machine, follow [these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).
* If you are cloning this project, skip all pip3 installs and run the following command to install all required libraries/packages at once:
    > pip install -r requirements.txt
* Please make sure you set up and activate virtual enviroment.

## Setting up the Workspace
* Install Django version 3.2:
    > pip install django==3.2.25
* Install django-allauth for account authentication
    > pip install django-allauth==0.41.0
* Install Django Crispy Forms:
    > pip install django-crispy-forms==1.14.0
* Install Django Countries:
    > pip install django-countries==7.2.1
* Install gunicorn:
    > pip install gunicorn
* Install supporting libraries:
    > pip install dj_database_url==0.5.0 psycopg2

    > pip install Pillow

    > pip install stripe
* Create `requirements.txt`: This file will list all the project dependencies, making it easy to install them in other environments.
    > pip freeze > requirements.txt
* Create a folder, and a project in that folder:
    > django-admin startproject <your_project_name> . (my project name was Niche_art_toys)
* Create an app within the project:
    > python manage.py startapp <your_app_name> (in my project it was home app)
* Add the new app to the list of installed apps in `setting.py`.
* Migrate changes:
    > python manage.py migrate
* Test server:
    > python manage.py runserver (You should see the default Django success page)


## Creating ElephantSQL Database

Assuming you have already created an account with ElephantSQL. 

* Click “Create New Instance”
* Set up your plan:
* Give your plan a Name.
* Select the plan.
* You can leave the Tags field blank.
* Select “Select Region”
* Click “Review”
* Check your details are correct and then click “Create instance”
* Return to the ElephantSQL dashboard and click on the database instance name for this project

## Creating Heroku App

Assuming you have already created an account with Heroku.

* Create a new Heroku app:
* Click "New" in the top right-hand corner of the main page, then click "Create new app"
* Give your app a name and select the region closest to you. When done, click "Create app" to confirm.
* Open the "Settings" tab. Add the config var DATABASE_URL, and for the value, copy in your database url from ElephantSQL.
* From your editor, go to your project's settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
* Left box under config vars (variable KEY) = SECRET_KEY
* Right box under config vars (variable VALUE) = Value copied from settings.py in project.

## AWS S3 Bucket  
Assuming you have already created an account with AWS.
* Create a new S3 bucket:
* Click "Services" in the top left-hand corner of the main page, select "S3"
* Click "Create bucket", give the bucket a unique name
* Select the nearest location
* Under the "Object Ownership" section, select "ACLS enabled"
* Under the "Bucket settings for Block Public Access", uncheck "Block all public access", and acknowledge that this will make the bucket public
* Click "Create bucket"
* Bucket settings:
    * Click on the bucket name, and then on the "Properties" tab
    * Under the "Static website hosting" section, click "Edit"
    * Under the "Static website hosting" section select "Enable"
    * Under the "Hosting type" section ensure "Host a static website" is selected
    * Under the "Index document" section enter "index.html"
    * Click "Save changes"
    * Bucket permissions:
    * Click on the "Permissions" tab
    * Scroll down to the "CORS configuration" section and click edit
    * Enter the following snippet into the text box:

```
    [
      {
          "AllowedHeaders": [
              "Authorization"
          ],
          "AllowedMethods": [
              "GET"
          ],
          "AllowedOrigins": [
              "*"
          ],
          "ExposeHeaders": []
      }
    ]
```

* Click "Save changes"
* Scroll back up to the "Bucket Policy" section and click "Policy generator"
* Select "S3 Bucket Policy" from the drop down menu
* Enter " * " in the "Principal" text box
* From the "Actions" drop down menu select "GetObject"
* Copy and paste the "ARN" from the bucket policy page into the "Amazon Resource Name (ARN)" text box.
* Click "Add Statement", and then "Generate Policy"
* Copy the policy and paste it into the bucket policy text box on the previous tab. In the same text box add "/*" to the end of the resource key to allow access to all resources in this bucket.
* Click "Save"
* Select "Access Control List" section, find "Public access" and click "Everyone" under it. In the "Access to the objects" pop up window, tick "List objects"
* Click "Save"
* Create AWS static files User and assign to S3 Bucket:
    * Create "User Group":
        * Click "Services" in the top left-hand corner of the main page
        * Under "Access management" click "Groups"
        * Click "Create New Group", enter Group Name
        * Scroll to the bottom of the page and click "Create Group"
    * Create permissions policy for the new user group:
        * Click "Policies" in the left-hand menu.
        * Click "Create Policy"
        * Click "Import managed policy"
        * Search for "AmazonS3FullAccess", select this policy, and click "Import"
        * Click "JSON" under "Policy Document" to see the imported policy
        * Copy the bucket ARN from the bucket policy page and paste it into the "Resource" section of the JSON snippet. Be sure to remove the default value of the resource key ("*") and replace it with the bucket ARN.
        * Copy the bucket ARN a second time into the "Resource" section of the JSON snippet. This time, add "/*" to the end of the ARN to allow access to all resources in this bucket
        * Click "Review Policy"
        * Enter a name for the policy and a description
        * Click "Create Policy"
    * Attach Policy to User Group:
        * Click "Groups" in the left-hand menu
        * Click on the user group name created during the above step
        * Click "Attach Policy"
        * Search for the policy created and select it
        * Click "Attach Policy"
    * Create User:
        * Click "Users" in the left-hand menu
        * Click "Add user"
        * Enter a "User name"
        * Select "Programmatic access" and click "Next"
        * Select "Add user to group"
        * Click "Next"
        * Click "Create user"
        * Take note of the "Access key ID" and "Secret access key" as these will be needed to connect to the S3 bucket
        * Click "Download .csv" to download the credentials
        * Click "Close"
* Install required packages to use AWS S3 Bucket in Django:
    > pip install boto3

    > pip install django-storages
* Add 'storages' to the bottom of the installed apps section of settings.py file.


## Environmental Variables
* Create a new env.py file in the project's root directory to securely store environment variables. This file is added to .gitignore to prevent sensitive information like API keys and database credentials from being exposed in version control.
* Import os library in env.py
    > import os
* Setup environment variables:
    > os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
* Add secret key (google gjango secret key generator or make up your own):
    > os.environ["SECRET_KEY"] = "your SecretKey"


## settings.py File
* At the top of your settings.py file add:

```
import os
from pathlib import Path
import dj_database_url
if os.path.isfile("env.py"):
  import env

SECRET_KEY = os.environ.get('SECRET_KEY', '')
```

* Enhanced the flexibility of the DATABASES configuration in settings.py by conditionally using Heroku Postgres in production and SQLite3 for local development. This approach streamlines database management across different environments.
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

* Configur Django to efficiently manage static and media files:

```
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```

* Add the following snippet to the end of the main project urls.py:
    > urlpatterns = [path('admin/', admin.site.urls),  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
* Within TEMPLATES array, add 'DIRS':[TEMPLATES_DIR] like the below example:

```
TEMPLATES = [
      {
          …,
          'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
    ],
          …,
          
        },
  ]

```

* Integrate Amazon S3 cloud storage into the Django project by configuring the necessary settings in settings.py:

```
if 'USE_AWS' in os.environ:
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'nichestore'
    AWS_S3_REGION_NAME = 'us-east-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

* Add allowed hosts to settings.py:
    > ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

* Create a Procfile within the project's root directory to define the web process type and command for running the application on Heroku, leveraging Gunicorn as the production web server.
    > web: gunicorn PROJECTNAME.wsgi:application

* Make an initial commit and push the code to the GitHub Repository

```
    git add .
    git commit -m "Initial deployment"
    git push
```

* Add AWS Keys (see above) to Heroku Config Vars
* Add the USE_AWS variable to Heroku Config Vars and set it to True
* Create a file called "custom_storages.py" in the project's root directory and add the following code:

```
      from django.conf import settings
      from storages.backends.s3boto3 import S3Boto3Storage


      class StaticStorage(S3Boto3Storage):
          location = settings.STATICFILES_LOCATION


      class MediaStorage(S3Boto3Storage):
          location = settings.MEDIAFILES_LOCATION

```

## Cloning and Forking

Forking a repository on GitHub creates a personal copy on your GitHub account, allowing you to freely experiment and modify the code without affecting the original project.

### To fork a repository:

* Go to the repository on GitHub.com.
* Click the **Fork** button in the top-right corner.
* Choose an owner for the fork (usually your own account).
* Optionally, rename your fork and add a description.
* Choose whether to copy all branches or just the default branch.
* Click **Create fork**.

Cloning a repository creates a local copy on your computer, allowing you to work on it offline. You can clone your fork or the original repository.

### To clone a repository using HTTPS:

* Go to the repository (or your fork) on GitHub.com.
* Click **Code**.
* Click the copy icon next to **HTTPS**.
* Open your terminal or command prompt.
* Use the following command, replacing `<HTTPS URL>` with the copied HTTPS address:

   > git clone <HTTPS URL>


### To clone a repository using SSH:

* Follow first two steps above for HTTPS.
* Click SSH and then copy the URL.
* Open your terminal or command prompt.
* Use the following command, replacing <SSH URL> with the copied SSH address:

    > git clone <SSH URL>

Please note: Using SSH requires you to have an SSH key set up on your GitHub account.


### To clone a repository using GitHub CLI:
* Follow first two steps above for HTTPS.
* Click GitHub CLI and then copy the command.
* Paste the command into your terminal or command prompt and execute it.

