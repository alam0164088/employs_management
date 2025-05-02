 
from rest_framework import serializers
from .models import Employer

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ('id', 'company_name', 'contact_person_name', 'email', 'phone_number', 'address', 'created_at')
        read_only_fields = ('id', 'created_at')

    def validate_email(self, value):
        if Employer.objects.filter(email=value, user=self.context['request'].user).exists():
            raise serializers.ValidationError("This email is already in use by another employer.")
        return value