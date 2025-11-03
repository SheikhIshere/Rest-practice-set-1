from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import(
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserprofileView,
    activating_account,
)


router = DefaultRouter()
router.register('profile', UserprofileView, basename='profile')

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', activating_account, name='activate'),
    path('', include(router.urls)),
]