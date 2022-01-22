from .base import *
from .base import env


# GENERAL

DEBUG = False
SECRET_KEY = env('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = ['blocks.skybluetrades.net']


# SECURITY

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


# CACHES

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': '',
#     }
# }


# EMAIL

DEFAULT_FROM_EMAIL = 'blocks@skybluetrades.net'
SERVER_EMAIL = 'blocks-admin@skybluetrades.net'
ADMINS = [('Ian', 'ian@skybluetrades.net')]
MANAGERS = [('Ian', 'ian@skybluetrades.net')]
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('MAILJET_SMTP_SERVER')
EMAIL_PORT = env('MAILJET_SMTP_PORT')
EMAIL_HOST_USER = env('MAILJET_SMTP_USER')
EMAIL_HOST_PASSWORD = env('MAILJET_SMTP_PASSWORD')
EMAIL_USE_TLS = True

