# authentication related imports 
from django.contrib.auth import(
    authenticate,
    login,
    logout,
    get_user_model
)
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# core rest framework imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status

# local imports
from .serializers import(
    RegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer
)
from .models import UserProfile

# django redirecting
from django.shortcuts import redirect

# user model
User = get_user_model()

# for sending mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import (
    urlsafe_base64_encode, 
    urlsafe_base64_decode
)
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string





# user Profile view class 
class UserprofileView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


# user registration view class
class UserRegistrationView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            # just creating token here 
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f'http://127.0.0.1:8000/activate/{uid}/{token}'

            # sending mail
            name = user.first_name + ' ' + user.last_name
            email_subject = 'Confirm Your Email Address'
            email_body = render_to_string(
                'mail/confirmaiton_mail.html', 
                {
                    # passing context for the email
                    'name': name, 
                    'confirm_link': confirm_link
                }
            )
                
            email = EmailMultiAlternatives(
                email_subject,
                '',
                to=[user.email],
            )
            email.attach_alternative(
                email_body,
                'text/html'
            )
            email.send()

        return Response(serializer.errors)            

def activating_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        # for debugging only
        print(e)
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')
    
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():            
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            # doing authentication
            if User.objects.filter(email=email).exists(): #can i use this :  or User.objects.filter(email=email) == 'admin@gmail.com'
                user = authenticate(email=email, password=password)
                if user:       
                    try:          
                        token, created = Token.objects.get_or_create(user=user)
                        login(request, user)
                        return Response({
                            'token': token.key,
                            'user': user.email
                        })
                    except:
                        return Response({
                            'error': 'account is not active yet'
                        })
                else:
                    return Response({
                        'error': 'Invalid credentials'
                    })    

            else:
                return Response({
                    'error': 'User not register yet'
                })

        return Response(serializer.errors)


# doing logout 
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)