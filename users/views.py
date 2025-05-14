"""Views for the Booking API."""
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .permissions import *
from .serializers import *


class BookingRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    """Class handling Retrieving and destroying a booking."""
    queryset = Booking.objects.all()

    permission_classes = [IsBookingOwnerOrAdmin]

    serializer_class = BookingSerializer


class EventBookingList(ListCreateAPIView):
    """Class handling listing and creating of bookings for an event."""
    serializer_class = EventBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        event = get_object_or_404(Event, pk=self.kwargs['pk'])
        return Booking.objects.filter(event=event)

    def perform_create(self, serializer):
        event = get_object_or_404(Event, pk=self.kwargs['pk'])
        serializer.save(event=event, user=self.request.user)
