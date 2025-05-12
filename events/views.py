from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Exists, OuterRef
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event
from users.models import Booking
from .serializers import *
# Create your views here.


""" def home(request):
    query_set = Event.objects.all().select_related('creator')[:10]
    return render(request, 'home.html', context={'name': 'eyad', 'events': query_set, 'title': 'Home'})


def about(request):
    return render(request, 'about.html', context={'title': 'About'})
 """


@api_view()
def event_list(request):
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


@api_view()
def event_details(request, id):
    event = get_object_or_404(Event, pk=id)
    serializer = EventSerialzer(event, context={'request': request})
    return Response(serializer.data)
