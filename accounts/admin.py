from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Bus, Booking

admin.site.register(Bus)
admin.site.register(Booking)
