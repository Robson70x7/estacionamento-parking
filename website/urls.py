from django.urls import include, path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home, name="home")
]