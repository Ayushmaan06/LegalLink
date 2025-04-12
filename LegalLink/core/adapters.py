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
        print("MyAccountAdapter.get_login_redirect_url called for", user.username)
        try:
            profile = user.userprofile
        except UserProfile.DoesNotExist:
            profile = None
        if not user.first_name or not (profile and profile.city):
            return 'http://localhost:8080/profile-setup'
        else:
            return 'http://localhost:8080/home'