from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class CategoryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


STAR = (
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),
)


class BookModel(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)  # Changed to ForeignKey (OneToOne would limit users to one book)
    
    # basic book info
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
    description = models.TextField()

    # attributes
    category = models.ManyToManyField(CategoryModel, blank=True)  # Removed null=True (not valid for ManyToMany)
    created_at = models.DateTimeField(auto_now_add=True)  # Fixed
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class ReviewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    feedback = models.TextField( null=True, blank=True)  # Changed to TextField for longer text
    star = models.IntegerField(choices=STAR)  # Changed to IntegerField
    created_at = models.DateTimeField(auto_now_add=True)  # Fixed
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.book.title}"  # Fixed: was returning non-existent field
    
    class Meta:
        unique_together = ('user', 'book')  # Prevent multiple reviews by same user for same book

class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment

class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)  # Changed to ForeignKey
    created_at = models.DateTimeField(auto_now_add=True)  # Fixed
    
    def __str__(self):
        return f"{self.user.username} likes comment {self.book.id}"
    
    class Meta:
        unique_together = ('user', 'book')  # Prevent duplicate likes