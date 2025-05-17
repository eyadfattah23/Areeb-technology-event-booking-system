"""Url configuration for the users app."""
from django.urls import path


from .views import BookingRetrieveDestroyAPIView, MyBookingsAPIView

urlpatterns = [
    path('bookings/<int:pk>/', BookingRetrieveDestroyAPIView.as_view(),
         name='booking-detail'),
    path('users/me/bookings/', MyBookingsAPIView.as_view(), name='my-bookings'),
]
