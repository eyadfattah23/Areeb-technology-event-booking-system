from django.db.models import Exists, OuterRef
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
