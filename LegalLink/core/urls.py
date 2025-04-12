from django.urls import path
from .views import profile_setup_api

urlpatterns = [
    path('profile-setup-api/', profile_setup_api, name='profile-setup-api'),
]