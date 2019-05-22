import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'vendor'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'apps'))

VERSION = 0.01

# ==============================================================================

DEBUG = True
MIDDLEWARE_DEBUG = True
# ==============================================================================
# FILE HANDLERS
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# ==============================================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WSGI_APPLICATION = 'wsgi.application'
ROOT_URLCONF = 'urls'

LOCALE_PATHS = (BASE_DIR + '/webapp/locale', )

SITE_ID = 1
SITE_DOWN = False

# PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_DIR = os.path.join(PROJECT_DIR, 'static')
# STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

PROJECT_ROOT = os.path.dirname(__file__)

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'webapp/static')

MEDIA_URL = '/media/'
MEDIA_DIR = os.path.join(BASE_DIR, 'webapp/media')
MEDIA_ROOT = os.path.join(BASE_DIR, 'webapp/media')

AWS_CONFIG_FILE = os.path.join(BASE_DIR, '.aws/config')
AWS_CREDENTIAL_FILE = os.path.join(BASE_DIR, '.aws/credentials')
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_REGION_NAME = 'us-east-1'
AWS_CLIENT_ID = ""


STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'webapp/static/'),
)
TEMPLATES_DIR = os.path.join(BASE_DIR, 'webapp/templates')
TEMPLATES_DIRS = (TEMPLATES_DIR,)

SECRET_KEY = 'm3=+qz-!)*j_+^fmv9)553f)ylx_epl0q-+#04l$!(&hgbe234s'

TEST_EMAIL_DIR = os.path.join(os.path.dirname(__file__), 'tmp', 'emails')

ADMINS = (
    ('developer', 'developer@mydomain.com'),
)
MANAGERS = ADMINS

CONTACT_RECIPIENTS = [
    'support@mydomain.com'
]

# ==============================================================================
# INTERNATIONALIZATION
# https://docs.djangoproject.com/en/1.9/topics/i18n/
# ==============================================================================

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
    ('tr', 'Turkish'),
    ('de', 'German'),
    ('fr', 'French'),
    ('ja', 'Japanese'),
)

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# ==============================================================================
# AUTH
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
# ==============================================================================

LOGIN_REDIRECT_URL = "/"
# LOGIN_URL = '/login/'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ==============================================================================
# DATABASE
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# ==============================================================================
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ==============================================================================

ALLOWED_HOSTS = []
ALLOWED_IP = []

# Application definition
DJANGO_CONTRIB_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
)
PROJECT_APPS = (
    "pages",
)

THIRD_PARTY_APPS = (
    'vendor.translatable',
)

INSTALLED_APPS = DJANGO_CONTRIB_APPS + PROJECT_APPS + THIRD_PARTY_APPS

# ==============================================================================
# MIDDLEWARE
# ==============================================================================

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==============================================================================
# TEMPLATES
# ==============================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                'apps.pages.cp.global_settings',
            ],
        },
    },
]

INTERNAL_IPS = ['127.0.0.1']

try:
    from settings_local import *
except ImportError:
    print("Couldn't find settings_local.py, no site settings loaded.")

# ~~END~~=======================================================================
