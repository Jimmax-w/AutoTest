from django.db import models


# Create your models here.

class Settings(models.Model):
    set_host = models.CharField('Host', max_length=200)
    set_value = models.CharField('System Settings', max_length=200)

    class Meta:
        verbose_name = 'System Settings'
        verbose_name_plural = 'System Settings'

    def __str__(self):
        return self.set_host
