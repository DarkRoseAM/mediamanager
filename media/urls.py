from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.MediaListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', views.MediaDetailView.as_view(), name='detail'),
)
