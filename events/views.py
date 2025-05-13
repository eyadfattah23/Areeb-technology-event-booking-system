from django.db.models import Exists, OuterRef, Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Event
from .permissions import *
from .serializers import *
from users.models import Booking
from .filters import EventFilter
# Create your views here.


class EventViewSet(ModelViewSet):

    serializer_class = EventSerialzer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = EventFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'date', 'time']
    permission_classes = [IsEventOwnerOrAdmin]

    def get_queryset(self):
        query_set = Event.objects\
            .select_related('creator')\
            .annotate(
                is_booked=Exists(Booking.objects.filter(
                    user=self.request.user,
                    event=OuterRef('pk'))),
                number_of_bookings=Count('bookings'))
        return query_set

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


""" 
@api_view(['GET', 'POST'])
def event_list(request):
    if request.method == "GET":
        user = request.user
        bookings_subquery = Booking.objects.filter(
            user=user,
            event=OuterRef('pk'))

        query_set = Event.objects.prefetch_related(
            'bookings').select_related('creator').annotate(
            is_booked=Exists(bookings_subquery))

        serializer = EventSerialzer(
            query_set, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = EventSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=request.user)
        return Response(serializer.data, status=201)


@api_view(['GET', 'PUT', 'PATCH'])
def event_details(request, id):
    event = get_object_or_404(Event, pk=id)
    serializer = EventSerialzer(event, context={'request': request})
    return Response(serializer.data)
 """
