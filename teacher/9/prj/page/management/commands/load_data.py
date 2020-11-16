from django.core.management.base import BaseCommand, CommandError

from page.models import Catalog, Product

lst = ['Car', 'Funiture', 'Food', 'Clothes']
lst2 = ['Car product', 'Funiture  product', 'Food  product', 'Clothes  product']


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
