"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from updates.views import (
    json_dummy_view,
    JsonDummyCBV,
    JsonDummyCBVWithMixin,
    SerializedListView,
    SerializedDetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dummy/', json_dummy_view),
    path('dummy/cbv/', JsonDummyCBV.as_view()),
    path('dummy/mixin/', JsonDummyCBVWithMixin.as_view()),
    path('dummy/serializer/detail/', SerializedDetailView.as_view()),
    path('dummy/serializer/list/', SerializedListView.as_view()),
    # if namespace is specified, we must mention app_name as well
    path('api/status/', include('status.api.urls', namespace='api-status')),
    # path('api/auth/jwt/', obtain_jwt_token),
    # path('api/auth/jwt/refresh/', refresh_jwt_token),
    path('api/auth/', include('accounts.api.urls', namespace='api-auth')),
    path('api/user/', include('accounts.api.user.urls', namespace='api-user')),
]
