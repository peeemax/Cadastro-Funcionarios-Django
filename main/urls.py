from atexit import register
from django import views
from django.urls import path
from .views import HomeView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
]