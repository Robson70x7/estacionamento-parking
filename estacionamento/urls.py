from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls

urlpatterns = [
    path('', include('website.urls', namespace='website')),
    path('sistema/', include('core.urls', namespace='core')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
