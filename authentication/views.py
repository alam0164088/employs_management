from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View
from .serializers import UserSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            login(request, user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({'error': 'Invalid credentials'}, status=400)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            logout(request)
            return Response({"message": "Successfully logged out"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'authentication/login.html', {'error': 'Invalid username or password'})
    return render(request, 'authentication/login.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('index')
        except Exception as e:
            return render(request, 'authentication/register.html', {'error': str(e)})
    return render(request, 'authentication/register.html')

def profile_page(request):
    if not request.user.is_authenticated:
        return redirect('login_page')
    return render(request, 'authentication/profile.html')

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_page')
    return render(request, 'authentication/logout.html')

class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)