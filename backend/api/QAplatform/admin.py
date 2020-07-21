from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.UserAddition)
admin.site.register(models.Room)
admin.site.register(models.UseTime)
admin.site.register(models.File)
admin.site.register(models.Status)
admin.site.register(models.Message)
