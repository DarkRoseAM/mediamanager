# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django.conf.urls import patterns, url

# Application Imports
from . import views

# =============================================================================
# GLOBALS
# =============================================================================

urlpatterns = patterns(
    '',
    url(r'^$', views.mediaTableView, name='table'),
    url(
        r'(?P<pk>\d+)/$',
        views.MediaDetailView.as_view(),
        name='detail',
    ),
)
