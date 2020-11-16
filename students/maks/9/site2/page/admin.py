from django.contrib import admin

# Register your models here.

from page.models import Page
from page.models import Catalog
from page.models import Product

class PageAdmin(admin.ModelAdmin):
	pass

class CatalogAdmin(admin.ModelAdmin):
	pass

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'catalog']
	list_filter = ['catalog']

admin.site.register(Page, PageAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Product, ProductAdmin)