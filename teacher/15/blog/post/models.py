from django.db import models

from pytils.translit import slugify

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    alias = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.alias = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
