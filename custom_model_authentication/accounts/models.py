from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        # defining the extra fields
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        # check if the user is superuser
        if not extra_fields.get('is_staff'):
            raise ValueError('go off you are not a staff')
        
        if not extra_fields.get('is_superuser'):
            raise ValueError('go off you are not a superuser')

        save = self.create_user(email, password, **extra_fields)
        return save
    


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # for admin
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=timezone.now())

    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']
    def __str__(self):
        return f'{self.first_name + " " + self.last_name}' or self.email

    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    bio = models.CharField(max_length=500, null=True, blank=True)
    contact_info = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return f'{self.user.name}' or f'{self.user.email}' 