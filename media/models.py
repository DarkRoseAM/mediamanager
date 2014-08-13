# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django.db import models

# =============================================================================
# CLASSES
# =============================================================================

class Media(models.Model):
    barcode = models.IntegerField()
    contenttype = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    manifestfile = models.FileField(upload_to='manifests', null=True)
    md5 = models.CharField(max_length=255, blank=True)
    mediafile = models.FileField(upload_to='media', null=True)
    releasedate = models.DateField()
    title = models.CharField(max_length=255, blank=True)
    version = models.CharField(max_length=255, blank=True)

    # =========================================================================
    # SPECIAL METHODS
    # =========================================================================

    def __unicode(self):
        return self.title

    # =========================================================================
    # PUBLIC METHODS
    # =========================================================================

    @models.permalink
    def get_absolute_url(self):
        return 'media:detail', (), {'pk': self.pk}
