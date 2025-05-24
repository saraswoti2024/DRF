from rest_framework import serializers
from .models import *

class StudentSerailzers(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'

    #database ma create hunxa save hunxa value if validate xa vane
    def create(self, validated_data):
       return Student.objects.create(**validated_data) ##key:value rakhxa
    
    def update(self,instance,validate_data):
        instance.name = validate_data.get('name')
        instance.roll_no = validate_data.get('roll_no')
        instance.address = validate_data.get('address')
        instance.save()
        return instance
    