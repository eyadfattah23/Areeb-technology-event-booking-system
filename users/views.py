"""Views for the Booking API."""
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
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


def login(request):
    """Home view."""
    return render(request, 'users/LoginForm.html')


class MyBookingsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        serializer = MyBookingsSerializer(bookings, many=True)
        return Response(serializer.data)
