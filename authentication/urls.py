from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/auth/login/', views.LoginView.as_view(), name='api_login'),
    path('api/auth/logout/', views.LogoutView.as_view(), name='api_logout'),
    path('api/auth/profile/', views.profile_page, name='profile'),
    path('api/auth/register/', views.RegisterView.as_view(), name='api_register'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
]