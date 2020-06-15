from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response

from accounts.api.user.serializers import UserDetailSerializer
from status.api.serializers import StatusInlineUserSerializer
from status.api.views import StatusAPIView
from status.models import Status

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    # read only permission
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(is_active=True)  # all active users
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}


# class UserStatusAPIView(generics.ListAPIView):
class UserStatusAPIView(StatusAPIView):
    serializer_class = StatusInlineUserSerializer
    # all APIs will use default pagination from main.py
    # pagination_class = ForumAPIPagination
    # search_fields = ('user__username', 'content')
    # ordering fields are applied to all views by default, search fields must
    # be mentioned explicitly

    def get_queryset(self):
        username = self.kwargs.get("username", None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)

    # Restricting post on user status endpoint
    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)
