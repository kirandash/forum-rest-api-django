from django.urls import path

from .views import (
    StatusListSearchAPIView,
    StatusAPIView,
    StatusCreateAPIView,
)

urlpatterns = [
    # path('', StatusListSearchAPIView.as_view()),
    path('', StatusAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    # path('<int:id>/', StatusDetailAPIView.as_view()),
    # path('<int:id>/update/', StatusUpdateAPIView.as_view()),
    # path('<int:id>/delete/', StatusDeleteAPIView.as_view()),
]

# Approach one
# /api/status/ -> List
# /api/status/create -> Create
# /api/status/12/ -> Detail
# /api/status/12/update -> Update
# /api/status/12/delete -> Delete

# Approach Two
# /api/status -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD

# Approach Three
# /api/status -> CRUD & LS
