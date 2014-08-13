# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django.db import models

# =============================================================================
# CLASSES
# =============================================================================

class Manifest(models.Model):
    md5 = models.CharField(max_length=255, primary_key=True)
    file = models.FileField(upload_to='manifests', null=True)

    # =========================================================================
    # PUBLIC METHODS
    # =========================================================================

    #@models.permalink
    #def get_absolute_url(self):
    #    return 'media:detail', (), {'pk': self.pk}

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

class Media(models.Model):
    md5 = models.CharField(max_length=255, primary_key=True)
    file = models.FileField(upload_to='media', null=True)

    data = models.ForeignKey(MediaData, related_name='files')

    # =========================================================================
    # PUBLIC METHODS
    # =========================================================================

    #@models.permalink
    #def get_absolute_url(self):
    #    return 'media:detail', (), {'pk': self.pk}

# =============================================================================

class Upload(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    manifest = models.ForeignKey(Manifest, related_name='uploads')
