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

class FileInstance(models.Model):
    root = 'generic'
    md5 = models.CharField(max_length=32, primary_key=True, editable=False)
    file = models.FileField(upload_to=root, null=True)

    # =========================================================================
    # SPECIAL METHODS
    # =========================================================================

    def __unicode(self):
        return self.file

    # =========================================================================
    # PUBLIC METHODS
    # =========================================================================

    def save(self, *args, **kwargs):
        md5 = hashlib.md5()

        for chunk in self.file.chunks():
            md5.update(chunk)

        self.md5 = md5.hexdigest()
        super(FileInstance, self).save(*args, **kwargs)

# =============================================================================

class Manifest(FileInstance):
    root = 'manifests'

# =============================================================================

class MediaData(models.Model):
    barcode = models.IntegerField()
    contenttype = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    releasedate = models.DateField()
    title = models.CharField(max_length=255, blank=True)
    version = models.CharField(max_length=255, blank=True)

    manifest = models.ForeignKey(Manifest, related_name='media')

    # =========================================================================
    # SPECIAL METHODS
    # =========================================================================

    def __unicode(self):
        return self.title

# =============================================================================

class Media(FileInstance):
    root = 'media'
    data = models.ForeignKey(MediaData, related_name='files')

# =============================================================================

class Upload(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    manifest = models.ForeignKey(Manifest, related_name='uploads')
