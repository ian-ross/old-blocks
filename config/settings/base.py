import os
from pathlib import Path

import environ


ROOT_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / '.env'))


# GENERAL

DEBUG = env.bool('DJANGO_DEBUG', False)
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [str(ROOT_DIR / 'locale')]


# DATABASE

DATABASES = { 'default': env.db('DATABASE_URL') }
DATABASES['default']['ATOMIC_REQUESTS'] = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# URLS

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


# APPS

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'crispy_bootstrap5',
    'django_bootstrap5',
    'magiclink',
]

LOCAL_APPS = [
    'core',
    'blocks',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# MIDDLEWARE

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'blocks.middleware.RedirectMiddleware',
]


# STATIC

STATIC_ROOT = str(ROOT_DIR / 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [ROOT_DIR / 'static']
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

os.makedirs(STATIC_ROOT, exist_ok=True)


# TEMPLATES

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ROOT_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'


# SECURITY

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'


# EMAIL

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_TIMEOUT = 5


# AUTHENTICATION

AUTH_USER_MODEL = 'blocks.User'

AUTHENTICATION_BACKENDS = [
    'magiclink.backends.MagicLinkBackend',
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL = 'magiclink:login'
LOGOUT_REDIRECT_URL = 'magiclink:login'
LOGIN_REDIRECT_URL = 'blocks:home'

MAGICLINK_LOGIN_TEMPLATE_NAME = 'blocks/login.html'
MAGICLINK_LOGIN_SENT_TEMPLATE_NAME = 'blocks/login_sent.html'
MAGICLINK_LOGIN_FAILED_TEMPLATE_NAME = 'blocks/login_failed.html'

MAGICLINK_REQUIRE_SIGNUP = False

MAGICLINK_EMAIL_TEMPLATE_NAME_TEXT = 'blocks/login_email.txt'
MAGICLINK_EMAIL_TEMPLATE_NAME_HTML = 'blocks/login_email.html'

BLOCKS_EMAIL_ALLOW_LIST = [
    '@skybluetrades.net',
    '@wania.net',
    'ritawania@gmail.com'
]

# --------------------  MORE HERE?  --------------------

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
