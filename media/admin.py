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
        'created_at',
        'md5',
        'file',
        'upload',
    )

    list_display = [
        'created_at',
        'md5',
        'file',
    ]

    list_display_links = ['file']


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
        'upload',
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

    fields = (
        'records',
        'files',
    )

    list_display = [
        'created_at',
        'manifest',
    ]

    list_filter = []

    search_fields = []

# =============================================================================
# EXECUTION
# =============================================================================

admin.site.register(models.File, FileAdmin)
admin.site.register(models.Record, RecordAdmin)
admin.site.register(models.Upload, UploadAdmin)
