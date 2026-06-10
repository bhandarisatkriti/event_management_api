from django.contrib import admin
from .models import Organizer,Event,Registration

# Register your models here.
admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(Registration)
