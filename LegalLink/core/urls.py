from django.urls import path
from .views import profile_setup_api, user_profile_update_api, update_avatar_api

urlpatterns = [
    path('profile-setup-api/', profile_setup_api, name='profile-setup-api'),
    path('user-profile/', user_profile_update_api, name='user_profile_update_api'),
    path('update-avatar/', update_avatar_api, name='update_avatar_api'),
]