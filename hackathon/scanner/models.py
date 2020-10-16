from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Model 1
class Category(models.Model):
    category = models.CharField(max_length = 20, blank = False, null = False, )

    def __str__(self):
        return f"{self.category}"


# Model 2
class RTO(models.Model):
    code = models.PositiveIntegerField(max_length = 2, )
    def __str__(self):
        return f"{self.code}";


# Model 3
class State(models.Model):
    state = models.CharField(max_length = 2, blank = False, null = False, )
    RTO_code = models.ManyToManyField(RTO, blank = False, default = None, )
    def __str__(self):
        return f"{self.state}";


# Model 4
class License(models.Model):
    DL_No = models.PositiveIntegerField(max_length = 7, )
    name = models.CharField(max_length = 70, )
    dateOfIssue = models.DateTimeField(auto_now = False, auto_now_add = False, )
    validTill = models.DateTimeField(auto_now = False, auto_now_add = False, )
    state = models.ForeignKey(State, on_delete = models.CASCADE, blank = False, default = None, )
    category = models.ManyToManyField(Category, blank = True, )
    picture = models.ImageField(upload_to='ProfilesPics')
