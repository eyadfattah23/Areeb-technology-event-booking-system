from rest_framework import serializers
from .models import Event


class EventSerialzer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField()

    number_of_bookings = serializers.SerializerMethodField()
    is_booked = serializers.BooleanField(read_only=True)

    def get_number_of_bookings(self, event: Event):
        return event.bookings.count()

    def get_is_booked(self, event: Event):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return event.bookings.filter(user=request.user).exists()
        return False

    class Meta:
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
        read_only_fields = ['number_of_bookings', 'is_booked']
