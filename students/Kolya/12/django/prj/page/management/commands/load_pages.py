from django.core.management.base import BaseCommand, CommandError

from page.models import Page


class Command(BaseCommand):

    def handle(self, *args, **options):
       print('Hello command!!!')
       Page.objects.all().delete()
       page1 = Page()
       page1.title = 'Index page'
       page1.content = 'content content'
       page1.save()

       page2 = Page()
       page2.title = 'Index page 2'
       page2.content = 'content content 2'
       page2.save()