from django.core.management.base import BaseCommand, CommandError
from shop.models import Category
from shop.models import Product

all_ctgr = ["Phones", "Clothes", "Food", "Ware"]
phones = ["Xiaomi", "IPhone", "Samsung", "Huawei"] 
clothes = ["Outerwear", "Underwear", "Shoes", "Headwear"]
food = ["Fish", "Bakery products", "Milk products", "Dessert"]
ware = ["Cups", "Plates", "Pans", "Cutlery"]


class Command(BaseCommand):

      def handle(self, *args, **options):
            print('shop is working!')
            Category.objects.all().delete()
            for i in all_ctgr:
                  c = Category()
                  c.name = i
                  c.save()
                  print(c)

                  Product.objects.all().delete()
                  for i in phones:
                        p = Product()
                        p.name = i
                        p.category = c
                        p.save()

                        '''Product.objects.all().delete()
                        for i in clothes:
                              d = Product()
                              d.name = i
                              d.category = c
                              d.save()'''

