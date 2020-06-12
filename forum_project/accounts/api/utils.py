import datetime
from django.conf import settings
from django.utils import timezone

expires_delta = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        # to show when the token will expire and ask user to refresh token
        'expires': timezone.now() + expires_delta -
        datetime.timedelta(seconds=200)  # 200 seconds to take care of
        # delay in API call etc
    }