"""Module defining classes responsible for the events admin page"""
from django.contrib import admin
from .models import *
from users.models import Booking


class EventBookingInline(admin.TabularInline):
    """Inline class for booking in the event admin page."""
    autocomplete_fields = ['user']
    model = Booking
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin class for the Event model."""
    list_display = ['id', 'title', 'category',
                    'custom_category', 'date', 'time', 'price', 'venue', 'creator__username']
    list_select_related = ['creator']

    list_per_page = 50

    search_fields = ['title__istartswith',
                     'title__iendswith', 'creator__username__istartswith']

    list_filter = ['price', 'date', 'category', 'time']
    autocomplete_fields = ['creator']
    inlines = [EventBookingInline]
