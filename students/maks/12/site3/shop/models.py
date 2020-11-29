from django.db import models
from django.utils.safestring import mark_safe
from image_cropping import ImageRatioField
from easy_thumbnails.files import get_thumbnailer
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

class Category(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=250)
	content = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default="", blank=True, null=True)
	image = models.ImageField(upload_to="")
	cropping = ImageRatioField('image', '430x360')

    @property
    def image_tag(self):
        return mark_safe("<img src= '%s' />" % self.image.url)
        
	def __str__(self):
		return self.name

class Busket(models.Model):
	name = models.CharField(max_length=100)
	number = models.TextField(max_length=100)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, default="", blank=True, null=True)

	def __str__(self):
		return self.name
