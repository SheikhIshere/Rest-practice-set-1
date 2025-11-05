from .views import (
    BookView,
    CategoryView,
    ReviewView,
    CommentView,
    LikeView
)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookView, basename='books')
router.register(r'categories', CategoryView, basename='categories')
router.register(r'reviews', ReviewView, basename='reviews')
router.register(r'comments', CommentView, basename='comments')
router.register(r'likes', LikeView, basename='likes')


urlpatterns = [
    path('', include(router.urls))
]