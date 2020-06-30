from django.shortcuts import render
from product.models import Product
from django.http import HttpResponseRedirect


# Create your views here.

def product_manage(request):
    message = ''
    if not request.session.get('is_login', None):
        message = 'Please login before manage products'
        # TODO：显示提示登录信息后自动跳转登录界面
        return HttpResponseRedirect('/login/')
    else:
        product_list = Product.objects.all()
        return render(request, 'products/product_manage.html', {
            "products": product_list
        })
