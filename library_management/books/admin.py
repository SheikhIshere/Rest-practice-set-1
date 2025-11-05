from django.contrib import admin
from .models import (
    BookModel,
    CategoryModel,
    ReviewModel,
    CommentModel,
    LikeModel    
)


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'uploader',
        'title',
        'author',
        'price',        
        'created_at'
    ]
    list_filter = [
        'uploader',
        'category',
        'price',
        'created_at'
    ]
    search_fields = [
        'title',
        'author',
        'uploader__username',
        'description'
    ]
    ordering = [
        '-created_at',
        'title'
    ]


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'title',
        'created_at'
    ]
    list_filter = [
        'user',
        'created_at'
    ]
    search_fields = [
        'title',
        'user__username'
    ]
    ordering = [
        'created_at'
    ]


@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'book',
        'star',
        'created_at'
    ]
    list_filter = [
        'user',
        'star',
        'created_at'
    ]
    search_fields = [
        'book__title',
        'user__username',
        'feedback'
    ]
    ordering = [
        '-created_at'
    ]


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'user',        
        'comment_preview',
        'created_at'
    ]
    list_filter = [
        'user',
        'created_at'
    ]
    search_fields = [
        'user__username',
        'comment_preview',
        'book__title'
    ]
    ordering = [
        '-created_at'
    ]
    
    def comment_preview(self, obj):
        return obj.comment[:50] + "..." if len(obj.comment) > 50 else obj.comment
    comment_preview.short_description = 'Comment'


@admin.register(LikeModel)
class LikeAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'book',
        'created_at'
    ]
    list_filter = [
        'user',
        'created_at'
    ]
    search_fields = [
        'user__username',
        'book__title'
    ]
    ordering = [
        '-created_at'
    ]