from django.contrib import admin
from .models import Year, Month, Day, Appointment

admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Day)
admin.site.register(Appointment)
