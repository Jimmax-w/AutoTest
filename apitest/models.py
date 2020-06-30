from django.db import models

from product.models import Product


# Create your models here.

class ApiTest(models.Model):
    Product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    ApiStep = models.ForeignKey('ApiStep', on_delete=models.CASCADE, null=True)
    api_test_name = models.CharField('Name', max_length=64)
    api_test_desc = models.CharField('Description', max_length=500, null=True)
    api_tester = models.CharField('Tester', max_length=64)
    apt_test_result = models.BooleanField('Result')
    create_time = models.DateTimeField('Create Time', auto_now=True)

    def __str__(self):
        return self.api_test_name


Request_Method = (
    ('POST', 'POST'),
    ('GET', 'GET'),
    ('PUT', 'PUT'),
    ('DELETE', 'DELETE'),
    ('PATCH', 'PATCH')
)


class ApiStep(models.Model):
    ApiTest = models.ForeignKey('ApiTest', on_delete=models.CASCADE)
    api_name = models.CharField('Name', max_length=100)
    api_url = models.CharField('Url', max_length=200)
    api_step = models.CharField('Step', max_length=100, null=True)
    api_param_value = models.CharField('Param_Value', max_length=800)
    api_method = models.CharField(verbose_name='Method', choices=Request_Method,
                                  default='GET', max_length=100, null=True)
    api_result = models.CharField('Result', max_length=200)
    api_status = models.BooleanField('Status')
    create_time = models.DateTimeField('Create Time', auto_now=True)

    def __str__(self):
        return self.api_name


class Apis(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    api_name = models.CharField('API Name', max_length=100)
    api_url = models.CharField('API Url', max_length=200)
    apt_param_value = models.CharField("Param_Value", max_length=800)
    api_method = models.CharField(verbose_name='Request Method', choices=Request_Method,
                                  default='GET', max_length=200)
    api_result = models.CharField('API RESULT', max_length=200)
    api_status = models.BooleanField('Pass')
    create_time = models.DateTimeField('Create Time', auto_now=True)

    class Meta:
        verbose_name = '單一場景接口'
        verbose_name_plural = '單一場景接口'

    def __str__(self):
        return self.api_name
