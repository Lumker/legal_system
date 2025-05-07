# deadlines/admin.py
from django.contrib import admin
from .models import Deadline

@admin.register(Deadline)
class DeadlineAdmin(admin.ModelAdmin):
    list_display = ('case', 'description', 'date', 'notified')
    list_filter = ('notified',)