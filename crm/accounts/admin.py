from django.contrib import admin
import inspect
from . import models

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj):
        admin.site.register(obj)
# Register your models here.
