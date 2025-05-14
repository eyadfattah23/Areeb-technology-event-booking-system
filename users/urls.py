"""Url configuration for the users app."""
from django.urls import path


from .views import BookingRetrieveDestroyAPIView

urlpatterns = [
    path('bookings/<int:pk>/', BookingRetrieveDestroyAPIView.as_view(),
         name='booking-detail')
]
