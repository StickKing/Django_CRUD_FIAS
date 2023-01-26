from django.contrib import admin
from atexit import register
from .models import Subject, District, CityGPT, Street, House, Flat, SorcName

# Register your models here.
admin.site.register(Subject)
admin.site.register(District)
admin.site.register(CityGPT)
admin.site.register(Street)
admin.site.register(House)
admin.site.register(SorcName)
admin.site.register(Flat)