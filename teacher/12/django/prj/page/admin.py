from django.contrib import admin

# Register your models here.

from page.models import Page, Catalog, Product

class PageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Page, PageAdmin)

class CatalogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Catalog, CatalogAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'catalog']
    list_filter = ['catalog']
admin.site.register(Product, ProductAdmin)



