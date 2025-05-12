from .models import *


from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):
    event = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='event-detail'
    )

    class Meta:
        model = Booking
        fields = [
            'user',
            'event',
            'booking_date'
        ]


class EventBookingSerializer(serializers.ModelSerializer):
    """ user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='user-detail'
    ) """

    class Meta:
        model = Booking
        fields = [
            'user',
            'event',
            'booking_date'
        ]
        read_only_fields = ['event', 'user']
