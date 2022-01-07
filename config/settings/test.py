from .base import *  # noqa
from .base import env

# GENERAL

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="very-secret-for-development",
)
TEST_RUNNER = "django.test.runner.DiscoverRunner"
