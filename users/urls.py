from django.urls import path, include


from .views import BookingRetrieveDestroyAPIView

urlpatterns = [
    path('bookings/<int:pk>/', BookingRetrieveDestroyAPIView.as_view(),
         name='booking-detail')
]
