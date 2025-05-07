# clients/admin.py
from django.contrib import admin
from .models import LawFirmUser, Client

@admin.register(LawFirmUser)
class LawFirmUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'firm_name', 'role')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'id_number', 'address')