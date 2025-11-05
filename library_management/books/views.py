from django.shortcuts import render
from .models import (
    BookModel,
    CategoryModel,
    ReviewModel,
    CommentModel,
    LikeModel
)
from .serializers import (
    BookSerializers,
    CategorySerializers,
    ReviewSerializer,
    CommentSerializer,
    LikeSerializer
)
from rest_framework import viewsets

# Create your views here

class BookView(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers

class CategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers

class ReviewView(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

class LikeView(viewsets.ModelViewSet):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer


