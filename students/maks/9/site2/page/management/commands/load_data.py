from django.core.management.base import BaseCommand, CommandError
from page.models import Catalog
from page.models import Product

lst = [ "Computers", "Laptops", "Phones", "Tablets"]
lst_2 = [ "Xiaomi", "Samsung", "Ipone", "Huawei"]

class Command(BaseCommand):

      def handle(self, *args, **options):
            print('Catalog is working!')
            Catalog.objects.all().delete()
            for i in lst:
                  c = Catalog()
                  c.name = i
                  c.save()

                  Product.objects.all().delete()
                  for i in lst_2:
                        d = Product()
                        d.name = i
                        d.catalog = c
                        d.save()