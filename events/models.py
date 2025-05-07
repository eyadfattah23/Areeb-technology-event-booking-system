"""Module to define Event class"""
from django.db import models
from django.core.exceptions import ValidationError


class Event(models.Model):
    """Model representing an event"""
    CATEGORY_FESTIVAL = 'FST'
    CATEGORY_PARTY = 'PAR'
    CATEGORY_SPORT = 'SPT'
    CATEGORY_CONFERENCE = 'CON'
    CATEGORY_WORKSHOP = 'WKS'
    CATEGORY_SEMINAR = 'SEM'
    CATEGORY_OTHER = 'OTH'

    CATEGORY_CHOICES = [
        (CATEGORY_FESTIVAL, 'Festival'),
        (CATEGORY_PARTY, 'Party'),
        (CATEGORY_SPORT, 'Sports events'),
        (CATEGORY_CONFERENCE, 'Conferences'),
        (CATEGORY_WORKSHOP, 'Workshop'),
        (CATEGORY_SEMINAR, 'Seminar'),
        (CATEGORY_OTHER, 'Other (Please specify...)'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(
        max_length=3, choices=CATEGORY_CHOICES, default="")
    custom_category = models.CharField(max_length=64, blank=True)
    description = models.TextField(max_length=1024)
    date = models.DateField()
    price = models.DecimalField(decimal_places=2)
    time = models.TimeField(blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    venue = models.CharField(max_length=255)
    location = models.URLField(null=True)
    img = models.ImageField(null=True, blank=True, upload_to="event_images/")

    def clean(self):
        """Custom validation to ensure that the custom category is filled
        when the category is set to 'Other'."""
        if self.category == self.CATEGORY_OTHER and not self.custom_category:
            raise ValidationError("Category not specified...")
