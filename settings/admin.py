from django.contrib import admin
from settings.models import Settings


# Register your models here.

class SettingsAdmin(admin.ModelAdmin):
    list_display = ['set_host', 'set_value', 'id']


admin.site.register(Settings)
