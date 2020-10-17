from django.contrib import admin

# Register your models here.

from .models import *

class LicenseAdmin(admin.ModelAdmin):
    filter_horizontal = ("category",)

admin.site.register(Category)
admin.site.register(RTO)
admin.site.register(State)
admin.site.register(License, LicenseAdmin)
