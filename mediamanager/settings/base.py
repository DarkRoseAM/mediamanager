""" Django settings for mediamanager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# =============================================================================
# IMPORTS
# =============================================================================

# Standard Imports
import os

# Third Party Imports
import dj_database_url

# =============================================================================
# GLOBALS
# =============================================================================

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = here('..')
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kz^(#_=)&ow$j-6@0tj@#3g)ct5&xiuv=o_q#ix*vjzc3jhiv-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Allen Rose', 'Allen@TheRoseEffect.com'),
)

ALLOWED_HOSTS = [
    '.herokuapp.com',
    '.herokuapp.com.',
]

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'south',
    'storages',
)

LOCAL_APPS = (
    'media',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mediamanager.urls'

WSGI_APPLICATION = 'mediamanager.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.config(),
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Amazon Web Service
AWS_STORAGE_BUCKET_NAME = 'tremediamanager'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Structure
MEDIA_ROOT = ''
MEDIA_URL = 'http://s3.amazonaws.com/{0}/'.format(AWS_STORAGE_BUCKET_NAME)

STATIC_ROOT = root('..', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    root('..', 'assets'),
)

TEMPLATE_DIRS = (
    root('templates'),
)
