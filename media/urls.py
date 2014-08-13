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
    url(r'^$', views.MediaListView.as_view(), name='list'),
    url(r'^manifest/$', views.uploader, name='uploader'),
    url(
        r'^(?P<slug>[\w-]+)/$',
        views.MediaDetailView.as_view(),
        name='detail',
    ),
)
