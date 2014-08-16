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


class File(models.Model):
    md5 = models.CharField(max_length=32, primary_key=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    file = models.FileField(upload_to='generic', null=True)

    upload = models.ForeignKey(Upload, related_name='files')

    # =========================================================================
    # PUBLIC METHODS
    # =========================================================================

    def save(self, *args, **kwargs):
        md5 = hashlib.md5()

        for chunk in self.file.chunks():
            md5.update(chunk)

        self.md5 = md5.hexdigest()
        super(FileInstance, self).save(*args, **kwargs)


class Record(models.Model):
    barcode = models.IntegerField()
    contenttype = models.CharField(max_length=255, blank=True)
    filename = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    md5 = models.CharField(max_length=32, blank=True)
    releasedate = models.DateField()
    title = models.CharField(max_length=255, blank=True)
    version = models.CharField(max_length=255, blank=True)

    upload = models.ForeignKey(Upload, related_name='records')


class Upload(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-created_at']
