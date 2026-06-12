from django.contrib import admin
from .models import Organizer,Event,Registration

# Register your models here.
class RegistrationInline(admin.TabularInline):
    model = Registration
    extra = 1


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ("id","name","email")
    search_fields = ("name","email")
    list_filter = ("name",)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id","title","venue","start_time","end_time","capacity")
    search_fields = ("title","venue",)
    list_filter = ("start_time", "end_time",)
    readonly_fields = ("created_at","updated_at",)
    inlines = [RegistrationInline]

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id',"user","event","registered_at",)
    search_fields = ("user__username","event__title",)
    readonly_fields = ("registered_at",)
    list_filter = ("registered_at","event")