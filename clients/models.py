from django.db import models
from django_cryptography.fields import encrypt
from django.contrib.auth.models import AbstractUser

# Internal Law Firm Users (lawyers, admins, etc.)
class LawFirmUser(AbstractUser):
    ROLE_CHOICES = [
        ('lawyer', 'Lawyer'),
        ('paralegal', 'Paralegal'),
        ('admin', 'Admin')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='lawyer')
    firm_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)

# External Clients (people/companies represented by the firm)
class Client(models.Model):
    name = models.CharField(max_length=255)
    id_number = encrypt(models.CharField(max_length=13))  # POPIA-compliant encryption
    address = models.TextField()
    contact_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_dashboard_permissions(self):
        return self.has_perm('dashboard.view_dashboard')