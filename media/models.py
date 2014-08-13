# =============================================================================
# IMPORTS
# =============================================================================

# Django Imports
from django.db import models
from django.template.defaultfilters import slugify

# =============================================================================
# CLASSES
# =============================================================================

class Media(models.Model):
    barcode = models.IntegerField()
    contenttype = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    md5 = models.CharField(max_length=255, blank=True)
    releasedate = models.DateField()
    slug = models.SlugField(max_length=255, blank=True, default='')
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
        return 'media:detail', (), {'slug': self.slug}

    # =========================================================================

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Media, self).save(*args, **kwargs)
