from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name='events-home'),
    path('events/', views.event_list),
    path('events/<int:id>/', views.event_details),
    # path('about/', views.about, name='about')
]
