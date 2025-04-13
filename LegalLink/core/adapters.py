from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from core.models import UserProfile

class MyAccountAdapter(DefaultSocialAccountAdapter, DefaultAccountAdapter):
    def new_user(self, request, sociallogin=None):
        # Check if sociallogin is provided; if not, delegate to the default account adapter.
        if sociallogin is None:
            return DefaultAccountAdapter.new_user(self, request)
        user = DefaultSocialAccountAdapter.new_user(self, request, sociallogin)
        return user

    def get_login_redirect_url(self, request):
        user = request.user
        profile = None
        # Attempt to get user's profile. Adjust this based on your UserProfile relation.
        if hasattr(user, 'userprofile'):
            profile = user.userprofile

        # If either first_name is missing or profile or profile.city is missing, redirect to profile setup.
        if not user.first_name or not (profile and getattr(profile, "city", None)):
            return "http://localhost:8080/profile-setup"
        else:
            return "http://localhost:8080/home"

    

    def is_open_for_signup(self, request, sociallogin):
        # Return True to allow new social signups.
        # You can add custom logic here if needed.
        return True