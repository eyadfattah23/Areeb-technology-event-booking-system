"""Views for the Booking API."""
from django.views.decorators.http import require_http_methods
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
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


class MyBookingsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        serializer = MyBookingsSerializer(bookings, many=True)
        return Response(serializer.data)


def login(request):
    """Home view."""
    return render(request, 'users/LoginForm.html')


@require_http_methods(["GET"])
def logout_view(request):
    """Handle user logout by clearing session and redirecting"""
    auth_logout(request)
    response = redirect('/login')
    response.delete_cookie('access_token')
    return response
