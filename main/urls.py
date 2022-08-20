from django.urls import path
from .views import HomeView, register
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    path('accounts/register', register, name='register')
]