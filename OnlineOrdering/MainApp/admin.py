from django.contrib import admin
from . import models

admin.site.register(models.login)
admin.site.register(models.items)
admin.site.register(models.donations)
admin.site.register(models.membership)