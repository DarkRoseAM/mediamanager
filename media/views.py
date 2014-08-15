# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView

# Application Imports
from .forms import UploadForm
from . import models
from .utils import process_upload

# =============================================================================
# CLASSES
# =============================================================================


class ManifestDetailView(DetailView):
    model = models.Manifest


class MediaDetailView(DetailView):
    model = models.Media


class MediaDataDetailView(DetailView):
    model = models.MediaData


class UploadDetailView(DetailView):
    model = models.Upload

# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================


def media_table_view(request, *args, **kwargs):
    template_name = 'media_table.html'

    test = None
    # Handle file upload.
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            test = process_upload(request.FILES['manifest'])

        #return HttpResponseRedirect(reverse('media:table'))

    # A empty, unbound form.
    form = UploadForm()

    # Load manifest_files for the list page.
    context = {
        'form': form,
        'test': test,
        #'media_files': [],
        #'uploads': Upload.objects.all(),
    }

    # Render list page with the manifest_files and the form.
    return render_to_response(
        template_name,
        context,
        context_instance=RequestContext(request),
    )
