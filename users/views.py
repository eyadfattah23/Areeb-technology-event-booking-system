from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Booking
from .permissions import *
from .serializers import *
# Create your views here.


class BookingRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Booking.objects.all()

    permission_classes = [IsBookingOwnerOrAdmin]

    serializer_class = BookingSerializer


class EventBookingList(ListCreateAPIView):
    serializer_class = EventBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        event = get_object_or_404(Event, pk=self.kwargs['pk'])
        return Booking.objects.filter(event=event)

    def perform_create(self, serializer):
        event = get_object_or_404(Event, pk=self.kwargs['pk'])
        serializer.save(event=event, user=self.request.user)
