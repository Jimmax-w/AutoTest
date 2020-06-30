from django.db import models
from product.models import Product


# Create your models here.

class AppCase(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    case_name = models.CharField('Case Name', max_length=200)
    test_result = models.BooleanField('Test Result')
    tester = models.CharField('Tester', max_length=32)
    create_time = models.DateTimeField('Create Time', auto_now=True)
    app_case_step = models.ForeignKey('apptest.AppCaseStep', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'App Testing Case'
        verbose_name_plural = 'App Testing Case'

    def __str__(self):
        return self.case_name


class AppCaseStep(models.Model):
    app_case = models.ForeignKey(AppCase, on_delete=models.CASCADE)
    test_step = models.CharField('Test Step', max_length=200)
    test_object_name = models.CharField('測試對象名稱', max_length=200)
    find_method = models.CharField('定位方式', max_length=200)
    ev_element = models.CharField('控件元素', max_length=800)
    operate_method = models.CharField('操作方法', max_length=200)
    test_data = models.CharField('測試數據', max_length=200, null=True)
    assert_data = models.CharField('驗證數據', max_length=200)
    test_result = models.BooleanField('Pass')
    create_time = models.DateTimeField('Create Time', auto_now=True)

    def __str__(self):
        return self.test_step
