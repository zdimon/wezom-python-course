from django.core.management.base import BaseCommand, CommandError
from post.models import Post

class Command(BaseCommand):
   

    def handle(self, *args, **options):
       for i in range(1,100):
           p = Post()
           p.title = 'Post number %s' % i
           p.content = 'Post content number %s' % i
           p.save()
           print('Saving %s' % i)