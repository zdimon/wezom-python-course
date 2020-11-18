from django.core.management.base import BaseCommand, CommandError
from shop.models import Page


class Command(BaseCommand):

    def handle(self, *args, **options):
       print('Hello command!!!')
       Page.objects.all().delete()
       page1 = Page()
       page1.title = 'Index page'
       page1.content = 'content content'
       page1.save()