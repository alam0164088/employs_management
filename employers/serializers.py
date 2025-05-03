from rest_framework import serializers
from .models import Employer

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['id', 'name', 'email', 'phone', 'address']