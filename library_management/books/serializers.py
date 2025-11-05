from rest_framework import serializers
from .models import (
    BookModel, 
    CategoryModel, 
    ReviewModel, 
    CommentModel,
    LikeModel
)


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            'id',
            'user',
            'title',
        ]
        read_only_fields = [
            'created_at',
            'updated_at',
        ]

class BookSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = BookModel
        fields = [
            'id',
            'uploader',
            'title',
            'author',
            'price',
            'pdf',
            'description',
            'category'
        ]
        read_only_fields = [
            'created_at',
            'updated_at'
        ]



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = [
            'id'
            'user',
            'book',
            'feedback',
            'star'
        ]
        read_only_fields = [
            'created_at',
            'updated_at'
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = [
            'id',
            'user',
            'book',
            'comment',            
        ]

        read_only_fields = [
            'created_at',
            'updated_at'
        ]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = [
            'id',
            'user',
            'book',
            
        ]
        read_only_fields = [
            'created_at',
            'updated_at'
        ]