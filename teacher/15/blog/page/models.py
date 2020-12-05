from django.db import models
#from django.template.defaultfilters import slugify
from pytils.translit import slugify
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
    title = models.CharField(verbose_name=_(u'Title2'),max_length=250)
    content = models.TextField(verbose_name=_(u'Content2'))
    alias = models.SlugField(verbose_name=_(u'Alias2'),null=True, blank=True)

    def save(self, *args, **kwargs):
        self.alias = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
