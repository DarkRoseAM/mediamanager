# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
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


class RecordDetailView(DetailView):
    model = models.Record


class UploadDetailView(DetailView):
    model = models.Upload

# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================


def table_view(request, *args, **kwargs):
    template_name = 'media_table.html'

    # Handle file upload.
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            upload = process_upload([request.FILES['file']])

        return HttpResponseRedirect(upload.get_absolute_url())

    # Load record for the list page.
    context = {
        'form': UploadForm(),
    }

    # Render list page with the record and the form.
    return render_to_response(
        template_name,
        context,
        context_instance=RequestContext(request),
    )
