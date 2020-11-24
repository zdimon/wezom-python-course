from django.contrib import admin
from django.urls import path

from page.views import index, product, saveorder

urlpatterns = [
    path('', index),
    path('product/<int:id>', product),
    path('saveorder', saveorder),
    path('admin/', admin.site.urls),
]
