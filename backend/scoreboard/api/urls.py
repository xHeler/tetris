from django.urls import path

from .views import PostList, ScoreDetail

urlpatterns = [
    path("<int:pk>/", ScoreDetail.as_view(), name="score_detail"),
    path("", PostList.as_view(), name="post_list"),
]
