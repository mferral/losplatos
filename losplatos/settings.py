"""
Django settings for losplatos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

#identificando la ruta del proyecto
import os
RUTA_PROYECTO=os.path.dirname(os.path.realpath(__file__))
URL_BASE='http://localhost:8000/'
#URL_BASE='http://201.173.156.95:8000/'
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('mikko', 'mferral@gmail.com'),
)

MANAGERS = ADMINS


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o40*ym=$1$4s^fu0$kfp+2q!i*+x82+39xxa)zbc3f3+qzuk%m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middleware.Evalua',
)

ROOT_URLCONF = 'losplatos.urls'

WSGI_APPLICATION = 'losplatos.wsgi.application'


TEMPLATE_DIRS = (
    os.path.join(RUTA_PROYECTO,'plantillas')
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',      # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'losplatos',                      # Or path to database file if using sqlite3.
        'USER': 'eldelosplatos',                      # Not used with sqlite3.
        'PASSWORD': '3ld3l0spl4t0s',                  # Not used with sqlite3.
        'HOST': '',                                # Set to empty string for localhost. Not used with sqlite3.
        #'HOST': '/tmp/mysql.sock',                # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                            # Set to empty string for default. Not used with sqlite3
     }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '/home/losplatos/webapps/losplatos/losplatos/'

STATIC_URL = 'http://losplatos.webfactional.com/static/'

STATICFILES_DIRS = (
    os.path.join(RUTA_PROYECTO,'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#se agrega para poder mostrar las variables de session,mensajes,static_url en el template
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
    #'myapp.context_processors.url_base',
)