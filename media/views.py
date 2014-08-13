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
from .models import Media
from .utils import getMedia

# =============================================================================
# CLASSES
# =============================================================================

class MediaDetailView(DetailView):
    model = Media

# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================

def mediaTableView(request, *args, **kwargs):
    template_name = 'media_table.html'

    # Handle file upload.
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            for media in getMedia(request.FILES['manifest']):
                media.save()

        return HttpResponseRedirect(reverse('media:table'))

    # A empty, unbound form.
    form = UploadForm()

    # Load manifest_files for the list page.
    context = {
        'form': form,
        'media_files': [],
        'uploads': Upload.objects.all(),
    }

    # Render list page with the manifest_files and the form.
    return render_to_response(
        template_name,
        context,
        context_instance=RequestContext(request),
    )
