"""Module Responsible for the events viewset"""
from django.db.models import Exists, OuterRef, Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Event
from .permissions import *
from .serializers import *
from .filters import EventFilter
from users.models import Booking
# Create your views here.


class EventViewSet(ModelViewSet):
    """Viewset for the Event model."""
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = EventFilter
    ordering_fields = ['price', 'date', 'time']
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    pagination_class = PageNumberPagination
    search_fields = ['title', 'description']
    serializer_class = EventSerializer

    def get_queryset(self):
        """Get the queryset for the Event model
        This method retrieves all events and annotates them with the number of
        bookings and whether the user has booked the event or not.
        """
        query_set = Event.objects\
            .select_related('creator')\
            .annotate(
                is_booked=Exists(Booking.objects.filter(
                    user=self.request.user,
                    event=OuterRef('pk'))),
                number_of_bookings=Count('bookings'))
        return query_set

    def perform_create(self, serializer):
        """Override the perform_create method to set the creator of the event."""
        serializer.save(creator=self.request.user)
