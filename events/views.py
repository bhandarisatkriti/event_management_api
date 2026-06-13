from django.shortcuts import render
from django.core.mail import send_mail
import textwrap

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Organizer, Event, Registration
from .serializers import OrganizerSerializer, EventSerializer, RegistrationSerializer


# Create your views here.
class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_parsers(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return [MultiPartParser(), FormParser()]
        return [JSONParser()]

    @action(
        detail=True,
        methods=["post"],
        url_path="register",
        permission_classes=[IsAuthenticated]
    )
    def register(self, request, pk=None):

        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required"},
                status=401
            )

        event = self.get_object()
        user = request.user

        registration, created = Registration.objects.get_or_create(
            user=user,
            event=event
        )

        if not created:
            return Response(
                {"message": "You already registered for this event"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if user.email:
            message = textwrap.dedent(f"""
                Hi {user.username},

                Thank you for registering for {event.title}! 🎊

                Your spot has been successfully reserved. We’re excited to have you join us.

                🔗 View your event details:
                http://localhost:8000/api/events/{event.id}/

                See you at the event!

                Best regards,  
                The Event Management Team
            """)

            send_mail(
                subject=f"🎉 Registration Confirmed: {event.title}",
                message=message,
                from_email="satkrit32@gmail.com",
                recipient_list=[user.email],
                fail_silently=False,
            )

        return Response(
            {"message": "Registered successfully and email sent"},
            status=status.HTTP_201_CREATED
        )


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    