from django.shortcuts import render
from .models import Product

# Create your views here.
from .forms import ProductCreateForm


def productcreate(request):
    


def index(request):
    product_list = Product.objects.all()
    product_dict = {'products': product_list}
    return render(request, 'index.html', product_dict, )
