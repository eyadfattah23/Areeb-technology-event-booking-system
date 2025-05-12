"""Module to define Event class"""
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models
from Config.settings import AUTH_USER_MODEL


class Event(models.Model):
    """Model representing an event"""
    CATEGORY_FESTIVAL = 'FST'
    CATEGORY_PARTY = 'PAR'
    CATEGORY_SPORT = 'SPT'
    CATEGORY_CONFERENCE = 'CON'
    CATEGORY_WORKSHOP = 'WKS'
    CATEGORY_SEMINAR = 'SEM'
    CATEGORY_MUSIC = 'MUS'
    CATEGORY_EDUCATION = 'EDU'
    CATEGORY_ART = 'ART'
    CATEGORY_TECH = 'TEC'
    CATEGORY_CULTURE = 'CUL'
    CATEGORY_EXHIBITION = 'EXH'
    CATEGORY_OTHER = 'OTH'

    CATEGORY_CHOICES = [
        (CATEGORY_PARTY, 'Party'),
        (CATEGORY_SPORT, 'Sports events'),
        (CATEGORY_CONFERENCE, 'Conferences'),
        (CATEGORY_WORKSHOP, 'Workshop'),
        (CATEGORY_SEMINAR, 'Seminar'),
        (CATEGORY_MUSIC, 'Music'),
        (CATEGORY_EDUCATION, 'Education'),
        (CATEGORY_ART, 'Art'),
        (CATEGORY_TECH, 'Technology'),
        (CATEGORY_CULTURE, 'Culture'),
        (CATEGORY_FESTIVAL, 'Festival'),
        (CATEGORY_EXHIBITION, 'Exhibition'),
        (CATEGORY_OTHER, 'Other (Please specify...)'),
    ]

    title = models.CharField(max_length=255, unique=True)
    category = models.CharField(
        max_length=3, choices=CATEGORY_CHOICES, default=CATEGORY_OTHER)
    custom_category = models.CharField(max_length=64, blank=True)
    description = models.TextField(max_length=1024)
    date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    time = models.TimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
    venue = models.CharField(max_length=255)
    location = models.URLField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to="event_images/")

    creator = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="created_events", null=True)

    class Meta:
        ordering = ['-date', '-time']
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['category'])
        ]

    def __str__(self):
        return f"{self.title} | id: {self.id}"

    def clean(self):
        """Custom validation for category and price attributes."""
        if self.category == self.CATEGORY_OTHER and not self.custom_category:
            raise ValidationError("Category not specified...")

        if self.price < 0:
            raise ValidationError('Price can\'t be negative')
        if (self.date == datetime.date.today() and self.time <= timezone.now().time()) or self.date < datetime.date.today():
            raise ValidationError(
                'Date and time must be in future not in the past')
