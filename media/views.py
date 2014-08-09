from django.views.generic import DetailView, ListView

from .models import Media


class PublishMediaMixin(object):
    def get_queryset(self):
        return self.model.objects.live()


class MediaDetailView(PublishMediaMixin, DetailView):
    model = Media


class MediaListView(PublishMediaMixin, ListView):
    model = Media
