from django.contrib import admin
from bug.models import Bug


# Register your models here.

class BugAdmin(admin.ModelAdmin):
    list_display = ['bug_name', 'bug_detail', 'bug_status', 'bug_level',
                    'bug_creater', 'bug_assign', 'created_time']


admin.site.register(Bug)
