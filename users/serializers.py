from .models import *
from rest_framework import serializers
from djoser.serializers import UserCreatePasswordRetypeSerializer, UserSerializer


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
    user = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = [
            'user',
            'booking_date'
        ]
        read_only_fields = ['event', 'user']


class CustomUserCreatePasswordRetypeSerializer(UserCreatePasswordRetypeSerializer):
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
    class Meta(UserSerializer.Meta):
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
        ]
        read_only_fields = ['email', 'id']
