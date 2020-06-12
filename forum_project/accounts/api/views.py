from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Import custom payload
from .utils import jwt_response_payload_handler

# Creating a new token manually
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
# Custom payload handler created by us
# jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

# payload = jwt_payload_handler(user)
# token = jwt_encode_handler(payload)

User = get_user_model()


class AuthView(APIView):
    permission_classes = [permissions.AllowAny]  # Must mention to overwrite
    # default settings from main.py

    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}
                            , status=400)
        data = request.data
        username = data.get('username') # username or email address
        password = data.get('password')
        user = authenticate(username=username, password=password)
        qs = User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact=username)
        ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                print(user)
                # From doc - Creating a new token manually
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request=request)
                # return Response({'token': token})
                return Response(response)
        return Response({"detail": "Invalid credentials"}, status=401)
