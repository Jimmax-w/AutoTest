from django.contrib import admin
from apptest.models import AppCase, AppCaseStep


# Register your models here.

class AppCaseStepAdmin(admin.TabularInline):
    list_display = ['test_step', 'test_object_name', 'find_method', 'ev_element',
                    'operate_method', 'test_data', 'assert_data', 'test_result',
                    'create_time', 'id', 'app_case']
    model = AppCaseStep
    extra = 1


class AppCaseAdmin(admin.ModelAdmin):
    list_display = ['case_name', 'test_result', 'tester', 'create_time', 'id']
    inlines = [AppCaseStepAdmin]


admin.site.register(AppCase, AppCaseAdmin)
