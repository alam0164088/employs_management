from django.urls import path
from .views import EmployerListCreateView, EmployerDetailView, employer_form

urlpatterns = [
    path('list/', EmployerListCreateView.as_view(), name='employer_list_create'),
    path('<int:pk>/', EmployerDetailView.as_view(), name='employer_detail'),
    path('form/', employer_form, name='employer_form'),
]