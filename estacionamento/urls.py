from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('sistema/', include('core.urls', namespace='core')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
