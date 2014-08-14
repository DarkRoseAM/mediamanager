# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django.contrib import admin
from .models import Manifest, Media, MediaData, Upload

# =============================================================================
# CLASSES
# =============================================================================

class ManifestAdmin(admin.ModelAdmin):
    fields = (
        'file',
    )

    list_display = [
        'md5',
        'file',
    ]

    list_display_links = ['file']

    list_filter = ['file']

# =============================================================================

class MediaAdmin(admin.ModelAdmin):
    fields = (
        'md5',
        'file',
        'data',
    )

    list_display = [
        'md5',
        'file',
        'data',
    ]

    list_display_links = ['file']

    list_filter = ['file']

# =============================================================================

class MediaDataAdmin(admin.ModelAdmin):
    date_hierarchy = 'releasedate'

    fields = (
        'title',
        'releasedate',
        'version',
        'contenttype',
        'language',
        'barcode',
        'manifest',
    )

    list_display = [
        'md5',
        'title',
        'releasedate',
        'version',
        'contenttype',
        'language',
        'barcode',
        'manifest',
        'files',
    ]

    list_display_links = ['title']

    list_filter = [
        'releasedate',
        'version',
        'contenttype',
        'language',
    ]

    search_fields = ['title']

# =============================================================================

class UploadAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'

    fields = (
        'manifest',
    )

    list_display = [
        'pk',
        'created_at',
        'manifest',
    ]

    list_filter = []

    search_fields = []

# =============================================================================
# EXECUTION
# =============================================================================

admin.site.register(Manifest, ManifestAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(MediaData, MediaDataAdmin)
admin.site.register(Upload, UploadAdmin)
