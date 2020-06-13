from django.urls import path
from accounts.api.user.views import UserDetailAPIView, UserStatusAPIView

app_name = 'detail'

urlpatterns = [
    path('<username>/', UserDetailAPIView.as_view(), name='detail'),
    path('<username>/status/', UserStatusAPIView.as_view(), name='list'),
]
