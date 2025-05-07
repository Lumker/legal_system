from django.db import models
from cases.models import Case

class Document(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    encrypted = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)