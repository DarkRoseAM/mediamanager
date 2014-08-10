from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView

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

urlpatterns += patterns(
    '',
    (r'^manifest/', include('mediamanager.media.urls')),
    (r'^$', RedirectView.as_view(url='/media/manifest_list/')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
