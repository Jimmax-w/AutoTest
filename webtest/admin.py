from django.contrib import admin
from webtest.models import WebCase, WebCaseStep


# Register your models here.


class WebCaseStepAdmin(admin.TabularInline):
    list_display = ['webCaseName', 'webStep', 'webObjName', 'webFindMethod', 'webElement', 'webOPtMethod',
                    'webTestData', 'webAssertData', 'webTestResult', 'createTime', 'id', 'webcase']
    model = WebCaseStep
    extra = 1


class WebCaseAdmin(admin.ModelAdmin):
    list_display = ['webCaseName', 'webTestResult', 'createTime', 'id']
    inlines = [WebCaseStepAdmin]


admin.site.register(WebCase, WebCaseAdmin)
