from django.contrib import admin
from apitest.models import ApiTest, ApiStep, Apis


# Register your models here.


class ApistepAdmin(admin.TabularInline):
    list_display = ['api_name', 'api_url', 'api_param_value', 'api_method',
                    'api_result', 'apt_status', 'create_time', 'id', 'apitest']
    model = ApiStep
    extra = 1


class ApitestAdmin(admin.ModelAdmin):
    list_display = ['api_test_name', 'api_tester', 'apt_test_result', 'create_time']
    inlines = [ApistepAdmin]


class ApisAdmin(admin.TabularInline):
    list_display = ['api_name', 'api_url', 'apt_param_value', 'api_method',
                    'api_result', 'api_status', 'create_time', 'id', 'product']


admin.site.register(ApiTest, ApitestAdmin)
admin.site.register(Apis)
