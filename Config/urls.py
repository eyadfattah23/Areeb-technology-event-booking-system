"""
URL configuration for Config project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from users.views import login as login_view
from events.views import event_list as event_list_view
admin.site.site_header = 'Areeb project admin page'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('api/', include('events.urls')),
    path('api/', include('users.urls')),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', login_view, name='login-home'),
    path('events/', event_list_view, name='events-home'),
    path('logout/', event_list_view, name='logout'),

]


if settings.DEBUG:
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
