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
        views.table_view,
        name='table',
    ),
    url(
        r'^record/(?P<pk>[\w-]+)/$',
        views.RecordDetailView.as_view(),
        name='record',
    ),
    url(
        r'^upload/(?P<pk>\d+)/$',
        views.UploadDetailView.as_view(),
        name='upload',
    ),
)
