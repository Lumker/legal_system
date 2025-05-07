# deadlines/models.py
from django.db import models
from cases.models import Case

class Deadline(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    notified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description} - {self.date}"