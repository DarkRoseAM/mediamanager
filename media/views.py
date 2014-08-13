# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView

# Application Imports
from .forms import ManifestForm
from .models import Media
from .utils import getMedia

# =============================================================================
# CLASSES
# =============================================================================

class MediaDetailView(DetailView):
    model = Media

# =============================================================================

class MediaListView(ListView):
    model = Media

# =============================================================================
# PUBLIC FUNCTIONS
# =============================================================================

def mediaTableView(request, *args, **kwargs):
    template_name = 'media_table.html'

    # Handle file upload.
    if request.method == 'POST':
        form = ManifestForm(request.POST, request.FILES)

        if form.is_valid():
            for media in getMedia(request.FILES['manifest'].read()):
                media.save()

        return HttpResponseRedirect(reverse('media:list'))

    form = ManifestForm()  # A empty, unbound form.

    # Load manifest_files for the list page.
    context = {'manifests': Media.objects.all(), 'form': form}

    # Render list page with the manifest_files and the form.
    return render_to_response(
        template_name,
        context,
        context_instance=RequestContext(request),
    )
