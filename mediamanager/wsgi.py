""" WSGI config for mediamanager project.

It exposes the WSGI callable as a module-level variable named 'application'.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

# =============================================================================
# IMPORTS
# =============================================================================

# Standard Imports
import os

# Django Imports
from django.core.wsgi import get_wsgi_application

# =============================================================================
# EXECUTION
# =============================================================================

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "mediamanager.settings",
)

application = get_wsgi_application()
