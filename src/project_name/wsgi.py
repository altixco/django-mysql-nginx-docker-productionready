"""
WSGI config for project_name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if 'PRODUCTION' in os.environ:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings.production")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings.development")

application = get_wsgi_application()
