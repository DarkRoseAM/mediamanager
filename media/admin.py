# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django.contrib import admin
from .models import Media

# =============================================================================
# CLASSES
# =============================================================================

class MediaAdmin(admin.ModelAdmin):
    date_hierarchy = 'releasedate'

    fields = (
        'title',
        'releasedate',
        'version',
        'contenttype',
        'language',
        'barcode',
        'md5',
        'manifestfile',
        'mediafile',
    )

    list_display = [
        'pk',
        'title',
        'releasedate',
        'version',
        'contenttype',
        'language',
        'barcode',
        'manifestfile',
        'mediafile',
    ]

    list_display_links = ['pk', 'title']

    list_editable = []

    list_filter = [
        'releasedate',
        'version',
        'contenttype',
        'language',
    ]

    search_fields = ['title']

# =============================================================================
# EXECUTION
# =============================================================================

admin.site.register(Media, MediaAdmin)
