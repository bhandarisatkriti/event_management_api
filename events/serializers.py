from rest_framework import serializers
from .models import Organizer, Event, Registration

class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizer
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"