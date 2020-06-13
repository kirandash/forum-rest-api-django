from django.contrib.auth import get_user_model
from rest_framework import generics

from accounts.api.user.serializers import UserDetailSerializer

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    # read only permission
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)  # all active users
    serializer_class = UserDetailSerializer
    lookup_field = 'username'
