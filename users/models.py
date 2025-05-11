"""Module to define CustomUser class"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from events.models import Event


class CustomUser(AbstractUser):
    """Custom user model extending the default Django user model
    To represent users"""
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        indexes = [
            models.Index(fields=['username'])
        ]

    def __str__(self):
        return f"{self.username} | id: {self.id}"


class Booking(models.Model):
    """Model to represent a booking"""
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='bookings')

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='bookings')

    booking_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')
