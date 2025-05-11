from django.contrib import admin

from datetime import timezone
from .models import *
# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category',
                    'custom_category', 'date', 'time', 'price', 'venue', 'creator__username']
    list_select_related = ['creator']

    list_per_page = 50

    search_fields = ['title__istartswith',
                     'title__iendswith', 'creator__username__istartswith']

    list_filter = ['price', 'date', 'category', 'time']
