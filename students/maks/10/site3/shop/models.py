from django.db import models

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

	def __str__(self):
		return self.name
