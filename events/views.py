from django.shortcuts import render
from rest_framework import viewsets
from .models import Organizer,Event,Registration
from .serializers import OrganizerSerializer,EventSerializer,RegistrationSerializer

# Create your views here.
class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer