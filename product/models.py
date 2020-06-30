from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField('Product Name', max_length=64)
    product_desc = models.CharField('Product Description', max_length=512)
    product_admin = models.CharField('Product Administrator', max_length=64)
    create_time = models.DateTimeField('Create Time', auto_now=True)

    class Meta:
        verbose_name = 'Product Manage'
        verbose_name_plural = 'Product Manage'

    def __str__(self):
        return self.product_name
