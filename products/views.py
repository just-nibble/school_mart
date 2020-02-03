from django.shortcuts import render

# Create your views here.


from products.models import Product


def index(request):
    product_list = Product.objects.all()
    product_dict = {'products': product_list}
    return render(request, 'index.html', product_dict, )
