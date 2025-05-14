"""Serializers for the Booking and CustomUser models."""
from .models import *
from rest_framework import serializers
from djoser.serializers import UserCreatePasswordRetypeSerializer, UserSerializer


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for the Booking model."""
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
    """Serializer for the Bookings related to an event."""
    user = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = [
            'user',
            'booking_date'
        ]
        read_only_fields = ['event', 'user']


class CustomUserCreatePasswordRetypeSerializer(UserCreatePasswordRetypeSerializer):
    """Serializer for creating a new user with password and re_password fields."""
    re_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = [
            'id',
            'username',
            'email',
            'password',
            're_password',
            'first_name',
            'last_name'
        ]


class CustomUserSerializer(UserSerializer):
    """Serializer for the CustomUser model."""
    class Meta(UserSerializer.Meta):
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
        ]
        read_only_fields = ['email', 'id']
