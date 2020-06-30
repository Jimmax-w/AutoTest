from django.contrib import admin
from product.models import Product
from apitest.models import Apis


# Register your models here.
class ApisAdmin(admin.TabularInline):
    list_display = ['api_name', 'api_url', 'apt_param_value', 'api_method',
                    'api_result', 'api_status', 'create_time', 'id', 'product']
    model = Apis
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list = ['id', 'product_name', 'product_desc', ' product_admin', 'create_time']
    inlines = [ApisAdmin]


admin.site.register(Product)
