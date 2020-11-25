from django.core.management.base import BaseCommand, CommandError

from page.models import Catalog, Product
from django.core.files import File
lst = ['Car', 'Funiture', 'Food', 'Clothes']
lst2 = ['Car product', 'Funiture  product', 'Food  product', 'Clothes  product']
from prj.settings import MEDIA_ROOT

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Loading catalog!!')
        Catalog.objects.all().delete()
        Product.objects.all().delete()
        for i in lst:
            c = Catalog()
            c.name = i
            c.save()
            for i in lst2:
                p = Product()
                p.name = i
                p.catalog = c
                p.save()
                p.image.save('%s.png' % p.id, File(open('%s/%s' % (MEDIA_ROOT,'bazuka.png'),'rb')))
