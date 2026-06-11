from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import OrganizerViewSet, EventViewSet, RegistrationViewSet

router = DefaultRouter()

router.register('organizers', OrganizerViewSet)

router.register('events', EventViewSet)

router.register('registrations', RegistrationViewSet)

urlpatterns = router.urls
