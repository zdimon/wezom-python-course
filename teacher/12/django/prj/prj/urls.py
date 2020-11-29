from django.contrib import admin
from django.urls import path

from page.views import index, product, saveorder, doregistration

urlpatterns = [
    path('', index),
    path('product/<int:id>', product),
    path('doregistration', doregistration),
    path('saveorder', saveorder),
    path('admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)