from django.contrib import admin

# Register your models here.

from .models import Event, Region

admin.site.register(Event)
admin.site.register(Region)
