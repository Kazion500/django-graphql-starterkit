from django.contrib import admin

# Register your models here.

from .models import Fruit, Color

admin.site.register(Fruit)
admin.site.register(Color)
