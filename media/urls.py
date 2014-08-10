from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.MediaListView.as_view(), name='list'),
    url(
        r'^(?P<slug>[\w-]+)/$',
        views.MediaDetailView.as_view(),
        name='detail',
    ),
)

urlpatterns += patterns(
    'mediamanager.media.views',
    url(r'^manifest_list/$', 'manifest_list', name='manifest_list'),
)
