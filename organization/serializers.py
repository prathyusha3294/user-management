from rest_framework import serializers
from organization.models import *

class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class UserSignInSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()