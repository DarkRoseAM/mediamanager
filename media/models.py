from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class MediaManager(models.Manager):
    def live(self):
        return self.model.objects.filter(published=True)


class Media(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    content = models.TextField()
    published = models.BooleanField(default=True)
    creator = models.ForeignKey(User, related_name='uploads')
    objects = MediaManager()

    class Meta:
        ordering = ['-created_at', 'title']

    def __unicode(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Media, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'media:detail', (), {'slug': self.slug}
