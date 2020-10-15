from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Model 1


class Category(models.Model):
    category = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return f"{self.category}"

# Model 2


class License(models.Model):
    name = models.CharField(max_length=70)
    dateOfIssue = models.DateTimeField(auto_now=False, auto_now_add=False)
