# =============================================================================
# IMPORTS
# =============================================================================

# Import
import hashlib

# Django Imports
from django.db import models

# =============================================================================
# CLASSES
# =============================================================================


class Upload(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-created_at']

    # =========================================================================
    # PUBLIC METHODS
    # =========================================================================

    def get_manifests(self):
        results = []
        for media in self.media:
            if media.is_manifest():
                results.append(media)

        return results

    def get_media(self):
        results = []
        for media in self.media:
            if not media.is_manifest():
                results.append(media)

        return results


class Media(models.Model):
    id = models.CharField(max_length=32, primary_key=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    file = models.FileField(upload_to='media', null=True)

    upload = models.ManyToManyField(Upload, related_name='media')

    # =========================================================================
    # PUBLIC METHODS
    # =========================================================================

    @models.permalink
    def get_absolute_url(self):
        return 'media:media', (), {'pk': self.pk}

    def get_id(self):
        md5 = hashlib.md5()
        for chunk in self.file.chunks():
            md5.update(chunk)

        return md5.hexdigest()

    def is_manifest(self):
        return self.records is not None

    def save(self, *args, **kwargs):
        self.id = self.get_id()
        super(Media, self).save(*args, **kwargs)


class Record(models.Model):
    id = models.CharField(max_length=32, primary_key=True, editable=False)

    barcode = models.IntegerField()
    contenttype = models.CharField(max_length=255, blank=True)
    filename = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    md5 = models.CharField(max_length=32, blank=True)
    releasedate = models.DateField()
    title = models.CharField(max_length=255, blank=True)
    version = models.CharField(max_length=255, blank=True)

    manifest = models.ManyToManyField(Media, related_name='records')

    # =========================================================================
    # PUBLIC METHODS
    # =========================================================================

    @models.permalink
    def get_absolute_url(self):
        return 'media:record', (), {'pk': self.pk}

    def get_id(self):
        properties = [
            'barcode',
            'contenttype',
            'filename',
            'language',
            'md5',
            'releasedate',
            'title',
            'version',
        ]

        md5 = hashlib.md5()
        for prop in properties:
            md5.update('{0}: {1},'.format(prop, getattr(self, prop)))

        return md5.hexdigest()

    def save(self, *args, **kwargs):
        self.id = self.get_id()
        super(Record, self).save(*args, **kwargs)
