from .base import *
from .base import env


# GENERAL

DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="very-secret-for-development",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]


# CACHES

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}


# DEBUG TOOLBAR

INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
