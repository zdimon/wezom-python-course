from page.models import Page

def page_processor(request):
    pages = Page.objects.all()            
    return {'pages': pages}