"""
Django settings for accountTracking project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from decouple import config
import os , sys , logging


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG' , default= False , cast = bool)

ALLOWED_HOSTS = [config('ALLOWED_HOSTS')]

# class Utf8StreamHandler(logging.StreamHandler):
#     def emit(self, record):
#         try:
#             msg = self.format(record)
#             if isinstance(msg, str):
#                 msg = msg.encode(sys.stdout.encoding or 'utf-8', 'replace')
#             elif isinstance(msg, bytes):
#                 msg = msg.decode('utf-8', 'replace').encode(sys.stdout.encoding or 'utf-8', 'replace')
#             stream = self.stream
#             stream.write(msg + self.terminator)
#             self.flush()
#         except Exception:
#             self.handleError(record)

### Logger as File
# LOGGING = {            
#     'version': 1,
#     'disable_existing_loggers': False,
#     "formatters": {
#         "verbose": {
#             "format": "{levelname} [{asctime}] {module} {process:d} {thread:d} {message}",
#             "style": "{",
#         },
#         "simple": {
#             "format": "({levelname}) [{asctime}] ({module}) : {message}",
#             "style": "{",
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'debug.log',
#             "formatter":"verbose" ,

#         },
#         "console":{
#             'level' : "DEBUG",
#             'class' : f'{__name__}.Utf8StreamHandler' ,
#             # 'class' : 'logging.StreamHandler' ,
#             "formatter": "verbose",
#             'stream': 'ext://sys.stdout',
#             # 'encoding': 'utf-8',  # Specify the encoding here
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ["file"],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#         "twitter":{
#             'handlers': ["console"],
#             'level': 'DEBUG',

#         }

#     },
# }
### Set encoding for console stream separately
# console_handler = LOGGING['handlers']['console']
# console_handler['stream'] = sys.stdout
# console_handler['stream'].encoding = 'utf-8'


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework' ,
    'corsheaders',
    'colorfield',
]

LOCAL_APPS = [
    'twitter'
]

INSTALLED_APPS = INSTALLED_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'accountTracking.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'accountTracking.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/static/",
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
}



CORS_ALLOWED_ORIGINS = [config("CORS_ALLOWED_ORIGINS")]

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored'
MEDIA_ROOT = BASE_DIR / 'media'

if DEBUG :
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    INTERNAL_IPS = ALLOWED_HOSTS
    
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.history.HistoryPanel',
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ]



# django_apscheduler Configuration
INSTALLED_APPS += ["django_apscheduler"]
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds




# # Celery Configuration Options
# CELERY_TIMEZONE = "Australia/Tasmania"
# CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60
# # Celery application definition
# CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_SERIALIZER = 'json'

