import json
import os.path

secrets = json.load(file(os.path.dirname(os.path.realpath(__file__ ))+"/../../secrets.json"))
main_path = secrets['MAIN_PATH']

DEBUG = (secrets['DEBUG'] == "TRUE")
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

#email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = secrets['EMAIL_HOST']
EMAIL_PORT = secrets['EMAIL_PORT']
EMAIL_HOST_USER = secrets['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = secrets['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = ("True" in secrets['EMAIL_USE_TLS'])

#who to email notifications to.
EMAIL_TO = secrets['EMAIL_TO']

DATABASES = {
    'default': {
        'ENGINE': secrets['DB_ENGINE'], 
        'NAME': secrets['DB_NAME'],                      
        'USER': secrets['DB_USER'],
        'PASSWORD': secrets['DB_PASSWORD'],
        'HOST': secrets['DB_HOST'],                      
        'PORT': secrets['DB_PORT'],                      
    }
}

ALLOWED_HOSTS = ['*']
TIME_ZONE = 'America/Toronto'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


MEDIA_ROOT = main_path+'cshub_site/static/'
MEDIA_URL = ''

STATIC_ROOT = '/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (main_path+'cshub_site/static',)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

SECRET_KEY = secrets['SECRET_KEY']

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


if DEBUG == False:
    MIDDLEWARE_CLASSES = ('django.middleware.cache.UpdateCacheMiddleware',) + MIDDLEWARE_CLASSES
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': '/var/run/redis/redis.sock',
        },
    }

ROOT_URLCONF = 'cshub_site.urls'
WSGI_APPLICATION = 'cshub_site.wsgi.application'

TEMPLATE_DIRS = (
    main_path+'cshub_site/registration_app/templates',
    main_path+'cshub_site/event_app/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'cshub_site',
    'event_app',
    'userprofile',
    'south',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#extending the user profile!
AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

TEMPLATE_CONTEXT_PROCESSORS = {
    "django.contrib.auth.context_processors.auth",
    'django.core.context_processors.request',
}

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = '/var/run/redis/redis.sock'

