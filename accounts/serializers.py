from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


# Create your models here.
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8,write_only=True)
    confirm_password = serializers.CharField(min_length=8,write_only=True)
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','password','email','confirm_password','user_type']
    
    def validate(self,data):
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        
        if username.lower() == password.lower():
            raise serializers.ValidationError('username and password shouldn\'t be same!')                               

        if password != confirm_password:
            raise serializers.ValidationError('confirm password and password should be same!') 
         
        return data 
        
    
    def validate_email(self,value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('email already exist!')
        return value
    
    def validate_password(self,value):    
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one number.")
        return value
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return CustomUser.objects.create_user(
            user_type = 'student',
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],    
            )

class Registration2serializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8,write_only=True)
    confirm_password = serializers.CharField(min_length=8,write_only=True)
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','password','email','confirm_password','user_type']
    
    def validate(self,data):
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        
        if username.lower() == password.lower():
            raise serializers.ValidationError('username and password shouldn\'t be same!')                               

        if password != confirm_password:
            raise serializers.ValidationError('confirm password and password should be same!') 
         
        return data 
        
    
    def validate_email(self,value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('email already exist!')
        return value
    
    def validate_password(self,value):    
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one number.")
        return value
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return CustomUser.objects.create_user(
            user_type = 'tutor',
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],    
            )