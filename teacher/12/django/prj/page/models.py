from django.db import models
from django.utils.safestring import mark_safe
from image_cropping import ImageRatioField
from easy_thumbnails.files import get_thumbnailer

class Page(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

class Catalog(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    content = models.TextField()
    catalog = models.ForeignKey(Catalog,on_delete=models.CASCADE, default='', blank=True, null=True)
    image = models.ImageField(upload_to='products')
    cropping = ImageRatioField('image', '100x100')

    @property
    def image_tag(self):
        return mark_safe('<img src="%s" />' % self.image.url)

    @property
    def image_crop_tag(self):
        thumbnail_url = get_thumbnailer(self.image).get_thumbnail({
            'size': (100, 100),
            'box': self.cropping,
            'crop': 'smart',
            'upscale': True,
        }).url
        return mark_safe('<img src="%s" />' % thumbnail_url)
        

    def __str__(self):
        return self.name

class Basket(models.Model):
    name = models.CharField(max_length=250)
    phone = models.TextField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE, default='', blank=True, null=True)

    def __str__(self):
        return self.name
