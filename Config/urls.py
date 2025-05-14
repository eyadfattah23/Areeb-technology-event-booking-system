"""
URL configuration for Config project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Areeb project admin page'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('api/', include('events.urls')),
    path('api/', include('users.urls')),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('__debug__/', include(debug_toolbar.urls))
]


if settings.DEBUG:
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
