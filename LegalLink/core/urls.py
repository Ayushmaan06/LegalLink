from django.urls import path
from .views import profile_setup_api, user_profile_update_api, update_avatar_api, user_cases_api, add_case_api, upvote_user_api

urlpatterns = [
    path('profile-setup-api/', profile_setup_api, name='profile-setup-api'),
    path('user-profile/', user_profile_update_api, name='user_profile_update_api'),
    path('update-avatar/', update_avatar_api, name='update_avatar_api'),
    path('user-cases/', user_cases_api, name='user_cases_api'),
    path('add-case/', add_case_api, name='add_case_api'),
    path('upvote-user/', upvote_user_api, name='upvote_user_api'),
]