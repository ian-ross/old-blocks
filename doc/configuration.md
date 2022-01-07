# Project configuration

All configuration is in `<project-root>/config`:

 - URLconfs are in `config/urls.py`.
 - ASGI and WSGI files are in `config`.
 - Settings are all in `config/settings`.
 

## Settings

 - Settings are split up by deployment type, with a `base.py` for
   shared settings and `local.py`, `test.py` and `production.py` for
   development, testing and deployment.

 - Secrets from environment variables using `django-environ`.
 

## Templates

 - Templates all use the Django template language.
 
 - All templates are in `<project-root>/apps/templates`.
 