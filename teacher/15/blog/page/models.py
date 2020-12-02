from django.db import models
#from django.template.defaultfilters import slugify
from pytils.translit import slugify

class Page(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    alias = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.alias = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
