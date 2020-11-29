from django.core.management.base import BaseCommand, CommandError
from shop.models import Category
from shop.models import Product
from django.core.files import File
import urllib
from site3.settings import MEDIA_ROOT

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
                        p.image.save("test.png",
                        File(open('%s/%s' % (MEDIA_ROOT, "icon128.png"), "rb"))
                        )

                        '''Product.objects.all().delete()
                        for i in clothes:
                              d = Product()
                              d.name = i
                              d.category = c
                              d.save()'''


