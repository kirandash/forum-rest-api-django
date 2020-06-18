from django.urls import path

from .views import (
    # StatusListSearchAPIView,
    StatusAPIView,
    # StatusCreateAPIView,
    StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView,
)

app_name = 'status'

urlpatterns = [
    # path('', StatusListSearchAPIView.as_view()),
    path('', StatusAPIView.as_view(), name='list'),
    # path('create/', StatusCreateAPIView.as_view()),
    # Add url name for reverse implementation
    path('<int:id>/', StatusDetailAPIView.as_view(), name='detail'),
    # path('<int:pk>/update/', StatusUpdateAPIView.as_view()),
    # path('<int:id>/delete/', StatusDeleteAPIView.as_view()),
]

# Approach one
# /api/status/ -> List
# /api/status/create -> Create
# /api/status/12/ -> Detail
# /api/status/12/update -> Update
# /api/status/12/delete -> Delete

# Approach Two with mixins
# /api/status -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD

# Approach Three with mixins
# /api/status -> CRUD & LS

# Best Approach with mixins
# /api/status -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD
