"""Django filters for the Event model."""
from django_filters.rest_framework import FilterSet
from .models import *


class EventFilter(FilterSet):
    """Event filter."""

    class Meta:
        """Meta class for EventFilter."""

        model = Event
        fields = {
            'title': ['icontains', 'exact'],
            'venue': ['icontains', 'exact'],
            'category': ['icontains', 'exact'],
            'custom_category': ['icontains', 'exact'],
            'creator__username': ['icontains'],
            'date': ['year__gt', 'year__lt', 'month__gt', 'month__lt', 'day__gt', 'day__lt'],
            'time': ['gt', 'lt'],
            'price': ['gt', 'lt'],
        }
