from django.urls import path
from .views import PostListView, CategoryListView

urlpatterns = [
    path("", PostListView.as_view(), name="list")
]
