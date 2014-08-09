from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.HomepageView.as_view(), name='home'),
    url(r'^media/', include('media.urls', namespace='media')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    })
)
