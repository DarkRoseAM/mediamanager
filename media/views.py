from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView

from .forms import ManifestForm
from .models import Media


class MediaDetailView(DetailView):
    model = Media


class MediaListView(ListView):
    model = Media


def manifest_list(request, *args, **kwargs):
    template_name = 'manifest_list.html'

    # Handle file upload.
    if request.method == 'POST':
        form = ManifestForm(request.POST, request.FILES)

        if form.is_valid():
            for values in parse_xml(request.FILES['manifest_file']):
                media = Media(**values)
                media.save()

            #return HttpResponseRedirect(reverse(
            #    'media:detail',
            #    args=['jurassic-park'],
            #))

        return HttpResponseRedirect(reverse('media:list'))

    form = ManifestForm()  # A empty, unbound form.

    # Load manifest_files for the list page.
    context = {'manifest_files': Media.objects.all(), 'form': form}

    # Render list page with the manifest_files and the form.
    return render_to_response(
        template_name,
        context,
        context_instance=RequestContext(request),
    )


def parse_xml(*args):
    return [{
        'barcode': '12345',
        'releasedate': '1980-06-12',
        'title': 'Blade Runner',
        'version': 'Directors Cut',
    }]
