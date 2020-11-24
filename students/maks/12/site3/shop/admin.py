from django.contrib import admin

# Register your models here.

from shop.models import Page
from shop.models import Category
from shop.models import Product
from shop.models import Busket

class PageAdmin(admin.ModelAdmin):
	pass
admin.site.register(Page, PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
	pass
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'category']
	list_filter = ['category']
admin.site.register(Product, ProductAdmin)

class BusketAdmin(admin.ModelAdmin):
	pass
admin.site.register(Busket, BusketAdmin)