# cases/models.py
from django.db import models
from clients.models import LawFirmUser, Client  # Import both models

class Case(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('pending', 'Pending')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    
    # ✅ Now using the correct Client model
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='cases')
    lawyer = models.ForeignKey(LawFirmUser, on_delete=models.SET_NULL, null=True, related_name='assigned_cases')
    
    court = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title