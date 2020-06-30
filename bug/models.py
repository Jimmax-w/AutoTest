from django.db import models
from product.models import Product


# Create your models here.

class Bug(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, null=True)
    bug_name = models.CharField('Bug Name', max_length=64)  # Bug 名称
    bug_detail = models.CharField('Details', max_length=200)  # 详情
    Bug_Status = (('Active', 'Active'), ('Solved', 'Solved'), ('Closed', 'Closed'))
    bug_status = models.CharField(verbose_name='Status', choices=Bug_Status,
                                  default='Active', max_length=200, null=True)
    BUG_LEVEL = (('1', '1'), ('2', '2'), ('3', '3'))
    bug_level = models.CharField(verbose_name='Bug Revel', choices=BUG_LEVEL,
                                 default='3', max_length=200, null=True)
    bug_creater = models.CharField('創建人', max_length=200)
    bug_assign = models.CharField('分配給', max_length=200)  # 分配给
    created_time = models.DateTimeField('Create Time', auto_now=True)  # 更新时间值

    class Meta:
        verbose_name = 'Bug Management'

    verbose_name_plural = 'Bug Management'

    def __str__(self):
        return self.bug_name
