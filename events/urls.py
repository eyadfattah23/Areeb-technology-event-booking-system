"""Url configuration for the events app."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from users.views import EventBookingList
router = DefaultRouter()
router.register('events', views.EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
    path('events/<int:pk>/bookings/',
         EventBookingList.as_view(), name='event-bookings')
]
