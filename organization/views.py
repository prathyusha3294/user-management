from django.shortcuts import render
from rest_framework import generics,mixins,viewsets,status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import UserSignUpSerializer,UserSignInSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token


def UserLogin(request):
    if request.method == 'POST':
        # Authentication logic here
        pass
    return render(request, 'login.html')

def Signup(request):
    if request.method == 'POST':
        # Authentication logic here
        pass
    return render(request, 'signup.html')
class UserSignUpViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer
    

    def create(self, request):
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data.get('email', None)
        create_password = serializer.validated_data.get('create_password', None)
        confirm_password = serializer.validated_data.get('confirm_password', None)
        
        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            return Response({"error": "User with this email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the passwords match
        if create_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the user instance with the hashed password
        user = User(
            first_name=serializer.validated_data['first_name'],
            last_name=serializer.validated_data['last_name'],
            email=email,
            phone_number=serializer.validated_data['phone_number'],
            create_password=make_password(create_password)  # Hash the password before saving
        )
        
        # Save the user to the database
        user.save()
        return Response({"message": "User Created Successfully"}, status=status.HTTP_201_CREATED)

        
         
class UserSignInViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSignInSerializer
     
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        if check_password(password, user.create_password):
            return Response({
                "Response": "User logged in successfully",
                "id": user.id,
                "firstname": user.first_name,
                "email": user.email,
                "mobile": user.phone_number if user.phone_number else None,
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Incorrect password."}, status=status.HTTP_400_BAD_REQUEST)
        
# class ForgetPasswordViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
#     permission_classes = [AllowAny]
#     serializer_class = Forget