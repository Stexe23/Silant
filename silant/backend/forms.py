
from django.core.exceptions import ValidationError
from django.http import request
from django.urls import reverse


class DefaultAccountAdapter:
    pass


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        if request.path.rstrip("/") == reverse("account_signup").rstrip("/"):
            return False
        return True


class DefaultSocialAccountAdapter:
    pass


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def validate_disconnect(self, account, accounts):
        raise ValidationError("Не удается отключить")
