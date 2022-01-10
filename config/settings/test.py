from .base import *
from .base import env


# GENERAL

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="very-secret-for-development",
)
TEST_RUNNER = "django.test.runner.DiscoverRunner"


# EMAIL

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
