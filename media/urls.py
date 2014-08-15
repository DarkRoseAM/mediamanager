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
    url(
        r'^$',
        views.media_table_view,
        name='table',
    ),

    url(
        r'^manifest/(?P<pk>[\w-]+)/$',
        views.ManifestDetailView.as_view(),
        name='manifest',
    ),

    url(
        r'^mediaDetail/(?P<pk>[\w-]+)/$',
        views.MediaDetailView.as_view(),
        name='media',
    ),

    url(
        r'^mediaData/(?P<pk>[\w-]+)/$',
        views.MediaDataDetailView.as_view(),
        name='mediaData',
    ),

    url(
        r'^upload/(?P<pk>\d+)/$',
        views.UploadDetailView.as_view(),
        name='upload',
    ),
)
