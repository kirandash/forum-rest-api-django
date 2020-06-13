from django.urls import path
from accounts.api.user.views import UserDetailAPIView

app_name = 'detail'

urlpatterns = [
    path('<username>/', UserDetailAPIView.as_view(), name='detail'),
]
