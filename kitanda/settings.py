import os
from datetime import timedelta
from functools import partial
from pathlib import Path
import dj_database_url
from decouple import Csv, config
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())
DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True
AUTH_USER_MODEL = 'core.User'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'cloudinary_storage',
    'cloudinary',
    'anymail',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'widget_tweaks',
    "sslserver",
    
    'kitanda.core.apps.CoreConfig',
    'kitanda.kitanda.apps.KitandaConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'kitanda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'kitanda.wsgi.application'

default_db_url = config('DATABASE_URL')
parse_database = partial(dj_database_url.parse, conn_max_age=600)
DATABASES = {
    'default': config('DATABASE_URL', default=default_db_url, cast=parse_database)
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


ACCOUNT_SESSION_REMEMBER = True

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Porto_Velho'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/' 

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hsnasn6ep',
    'API_KEY': '369633374136476',
    'API_SECRET': 'hzAvrmoLjGg2HkQOWISel_amL6Q'
}
    
MEDIA_URL = '/media/'
     
DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django allauth
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
LOGIN_ON_EMAIL_CONFIRMATION = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7


EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
DEFAULT_FROM_EMAIL = 'no-reply@kitanda.shop'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
ANYMAIL = {
    "MAILGUN_API_KEY": config('MAILGUN_API_KEY', default=''),
    "MAILGUN_SENDER_DOMAIN": config('MAILGUN_SENDER_DOMAIN', default=''),
}

db_from_env = dj_database_url.config(conn_max_age=0, ssl_require=False)
django_heroku.settings(locals(), databases=False)

# PAYMENT API

MERCADO_PAGO_PUBLIC_KEY = config('MERCADO_PAGO_PUBLIC_KEY', default='')
MERCADO_PAGO_ACCESS_TOKEN = config('MERCADO_PAGO_ACCESS_TOKEN', default='')
