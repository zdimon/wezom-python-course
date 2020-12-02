from django.forms import ModelForm
from page.models import Product

# Create the form class.
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'content', 'catalog', 'image']