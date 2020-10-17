from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.db.models import *


# Model 1
class Category(models.Model):
    category = models.CharField(max_length = 20, blank = False, null = False, )
    desc = models.CharField(max_length = 200, blank = False, null = False, default = "NA")

    def __str__(self):
        return f"{self.category}  -  {self.desc}"


# Model 2
class RTO(models.Model):
    code = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.code}";


# Model 3
class State(models.Model):
    state = models.CharField(max_length = 2, blank = False, null = False, )

    def __str__(self):
        return f"{self.state}";


# Model 4
class License(models.Model):
    # user = models.ForeignKey(, on_delete = models.CASCADE, blank = False, default = None, )
    DL_No = models.PositiveIntegerField()
    name = models.CharField(max_length = 70, )
    dateOfIssue = models.DateTimeField(auto_now = False, auto_now_add = False, )
    validTill = models.DateTimeField(auto_now = False, auto_now_add = False, )
    state = models.ForeignKey(State, on_delete = models.CASCADE, blank = False, default = None, )
    RTO = models.ForeignKey(RTO, on_delete = models.CASCADE, blank = False, )
    category = models.ManyToManyField(Category, blank = True, )
    picture = models.ImageField(upload_to='ProfilesPics')

    def __str__(self):
        return f"{self.id} : {self.DL_No}";
