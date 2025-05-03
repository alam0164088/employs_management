from rest_framework import generics, permissions
from django.shortcuts import render
from .models import Employer
from .serializers import EmployerSerializer

class EmployerListCreateView(generics.ListCreateAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

def employer_form(request):
    return render(request, 'employers/employer_form.html')