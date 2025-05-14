"""Module for serializing Event model data."""
from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """Serializer for the Event model."""
    creator = serializers.StringRelatedField()

    number_of_bookings = serializers.IntegerField(read_only=True)
    is_booked = serializers.BooleanField(read_only=True)

    class Meta:
        """Meta class for EventSerializer."""
        model = Event

        fields = [
            'id',
            'title',
            'category',
            'custom_category',
            'description',
            'date',
            'price',
            'time',
            'last_modified',
            'date_added',
            'venue',
            'location',
            'img',
            'number_of_bookings',
            'creator',
            'is_booked'
        ]
