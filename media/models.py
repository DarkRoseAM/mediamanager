from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Media(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    version = models.CharField(max_length=255, blank=True)
    releasedate = models.DateField()
    contenttype = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=255, blank=True)
    barcode = models.IntegerField()
    md5 = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='mediafiles')

    def __unicode(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Media, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'media:detail', (), {'slug': self.slug}
