Event Management API

A Django REST Framework backend project for managing events, organizers, and user registrations.

Installed dependencies:
~~~bash
uv add django
uv add djangorestframework
uv add djangorestframework-simplejwt
uv add drf-yasg
uv add django-jazzmin
uv add Pillow
uv add django-environ
uv add django-filter
~~~

Created three models:
Organizer, Events, Registrartion

Created seralizers and ModelViewSet for each model
Configured DefaultRouter for automatic URL generation
Customized Django admin using Jazzmin with ModelAdmin configurations including list display, search, filters, readonly fields, and inline registration support for Organizer, Event, and Registration models.
