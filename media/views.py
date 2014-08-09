from django.views.generic import DetailView, ListView

from .models import Media


class MediaDetailView(DetailView):
    model = Media


class MediaListView(ListView):
    model = Media
