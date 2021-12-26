from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    message = models.CharField(max_length=500)
    created = models.DateField()

    def __str__(self):
        return self.name


