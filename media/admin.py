# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django.contrib import admin

# Application Imports
from . import models

# =============================================================================
# CLASSES
# =============================================================================


class FileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'

    fields = (
        'file',
        'upload',
    )

    list_display = [
        'created_at',
        'file',
        'id',
    ]

    list_display_links = ['file']

    list_filter = [
        'created_at',
        'file',
    ]


class RecordAdmin(admin.ModelAdmin):
    date_hierarchy = 'releasedate'

    fields = (
        'title',
        'releasedate',
        'version',
        'contenttype',
        'language',
        'barcode',
        'md5',
        'filename',
        'manifest',
    )

    list_display = [
        'title',
        'releasedate',
        'version',
        'contenttype',
        'language',
        'barcode',
        'md5',
        'filename',
    ]

    list_display_links = ['title']

    list_filter = [
        'releasedate',
        'version',
        'contenttype',
        'language',
    ]

    search_fields = ['title']


class UploadAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'

    fields = ()

    list_display = [
        'pk',
        'created_at',
    ]

    list_filter = [
        'created_at',
    ]

# =============================================================================
# EXECUTION
# =============================================================================

admin.site.register(models.ManifestFile, FileAdmin)
admin.site.register(models.MediaFile, FileAdmin)
admin.site.register(models.Record, RecordAdmin)
admin.site.register(models.Upload, UploadAdmin)
