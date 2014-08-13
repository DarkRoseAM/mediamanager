from django.contrib import admin
from .models import Media


class MediaAdmin(admin.ModelAdmin):
    date_hierarchy = 'releasedate'

    fields = (
        'title',
        'slug',
        'releasedate',
        'version',
        'contenttype',
        'language',
        'barcode',
        'md5',
    )

    list_display = [
        'title',
        'releasedate',
        'version',
        'contenttype',
        'language',
        'barcode',
    ]

    list_display_links = ['title']

    list_editable = []

    list_filter = [
        'releasedate',
        'version',
        'contenttype',
        'language',
    ]

    prepopulated_fields = {'slug': ('title',)}

    search_fields = ['title']

admin.site.register(Media, MediaAdmin)
