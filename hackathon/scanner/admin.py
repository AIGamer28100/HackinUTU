from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Category)
admin.site.register(RTO)
admin.site.register(State)
admin.site.register(License)
