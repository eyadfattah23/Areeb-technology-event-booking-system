from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Exists, OuterRef
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Event
from users.models import Booking
from .serializers import *
# Create your views here.


class EventViewSet(ModelViewSet):

    serializer_class = EventSerialzer

    def get_queryset(self):
        query_set = Event.objects\
            .prefetch_related('bookings')\
            .select_related('creator')\
            .annotate(is_booked=Exists(Booking.objects.filter(
                user=self.request.user,
                event=OuterRef('pk'))))
        return query_set

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
