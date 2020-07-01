from django.db import models
from product.models import Product


# Create your models here

class WebCase(models.Model):
    products = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    webCaseName = models.CharField('測試用例名稱', max_length=200)
    webTestResult = models.BooleanField('測試結果')
    tester = models.CharField('Tester', max_length=16)
    createTime = models.DateTimeField('Create Time', auto_now=True)

    class Meta:
        verbose_name = 'Web Test Case'
        verbose_name_plural = 'Web Test Case'

    def __str__(self):
        return self.webCaseName


class WebCaseStep(models.Model):
    webcase = models.ForeignKey('WebCase', on_delete=models.CASCADE)
    webCaseName = models.CharField('測試用例標題', max_length=200)
    webStep = models.CharField('測試步驟', max_length=200)
    webObjName = models.CharField('測試對象名稱', max_length=200)
    webFindMethod = models.CharField('定位方式', max_length=200)
    webElement = models.CharField('控件元素', max_length=200)
    webOptMethod = models.CharField('操作方法', max_length=200)
    webTestData = models.CharField('測試數據', max_length=200, null=True)
    webAssertData = models.CharField('驗證數據', max_length=200)
    webTestResult = models.BooleanField('測試結果')
    createTime = models.DateTimeField('Create Time', auto_now=True)

    def __str__(self):
        return self.webCaseName
