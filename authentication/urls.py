from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/page/', views.register_page, name='register_page'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('login/page/', views.login_page, name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout/page/', views.logout_page, name='logout_page'),
    path('profile/', views.profile_page, name='profile'),
]