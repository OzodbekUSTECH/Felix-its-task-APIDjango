from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.Material)
admin.site.register(models.ProductMaterial)
admin.site.register(models.Warehouse)