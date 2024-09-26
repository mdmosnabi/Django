import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-whcs%-uu%k8f&m4suemxks@4!yu_an+@c(mxzrdsl$$v)-mu8t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'userauths',
    'channels',
    'rest_framework',
    
    # third party app
    'taggit',
    'ckeditor','ckeditor_uploader',
    
    # custom app
    'core',
    'Support',
    'custom_admin',
    
]
AUTH_USER_MODEL = 'userauths.User'

MIDDLEWARE = [
    # defult middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # custom middleware   
    'custom_admin.middleware.CustomAdminAuthMiddleware',
]

LOGIN_URL = '/staf/login/'

ROOT_URLCONF = 'ecommpro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join( BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'ecommpro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "Library Admin",
    "site_header": "MY SHOP",
    "site_brand": "MY SHOP",
    "site_logo": "img/natural.jpg",
    "welcome_sign": "Welcome to MY SHOP",
    "copyright": " MY SHOP",
}

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'skin':'moono',
        'codeSnippet_theme':'monokai',
        'toolbar': 'all',
        'extraPlugins':','.join(
            [
                'codesnippet',
                'widget',
                'dialog'
            ]
        ),
        'filebrowserBrowseUrl': '/ckeditor/browse/',
        'filebrowserUploadUrl': '/ckeditor/upload/',
        
    },
}


BKASH_APP_KEY = 'your_app_key' # bkash will provide am app_key
BKASH_APP_SECRET = 'your_app_secret'  # bkash will provide an app_secret
BKASH_USERNAME = 'your_username' # bkash will provide an usernaame
BKASH_PASSWORD = 'your_password' # bkash will provide a password
 # after complete devoloping work use "https://checkout.bka.sh/v1.2.0-beta" this url for production
BKASH_BASE_URL = 'https://checkout.sandbox.bka.sh/v1.2.0-beta'  # For sandbox, use production URL when going live

ASGI_APPLICATION = 'ecommpro.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

