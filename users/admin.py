from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email',
                    'first_name', 'last_name', 'is_staff', 'is_active']
    list_per_page = 50

    search_fields = ['username__istartswith', 'username__iendswith', 'email']
    list_filter = ['is_staff', 'is_active']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user__id', 'user__username', 'user__email',
                    'event__id', 'event__title', 'booking_date']

    list_select_related = ['user', 'event']
    autocomplete_fields = ['user', 'event']
    search_fields = ['event__id', 'event__title',
                     'user__username', 'user__email']
