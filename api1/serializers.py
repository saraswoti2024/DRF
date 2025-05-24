from rest_framework import serializers
from .models import *

class StudentSerailzers(serializers.Serializer):

    ##validators 
    def chare(value):
        for c in value:
         if c.isupper():
            raise serializers.ValidationError("it should be in lower case")
        return value

    name = serializers.CharField(max_length=100, validators = [chare])
    roll_no = serializers.IntegerField()
    address = serializers.CharField(max_length=100)

    # class Meta:
    #     model = Student
    #     fields = '__all__'

    #database ma create hunxa save hunxa value if validate xa vane
    def create(self, validated_data):
       return Student.objects.create(**validated_data) ##key:value rakhxa
    
    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.roll_no = validate_data.get('roll_no',instance.roll_no)
        instance.address = validate_data.get('address',instance.address)
        instance.save()
        return instance
    
    ##field level validation
    def validate_roll_no(self,value):
        if value>200:
            raise serializers.ValidationError('seat Full')
        if Student.objects.filter(roll_no=value).exists():
            raise serializers.ValidationError('already exists, use another number less than 200')
    
        return value
      
    ##object level validation
    def validate(self,data):
        address = data.get('address')
        name = data.get('name')
        city = ['kathmandu','bhaktapur','biratnagar','lalitpur','hetauda']
        for c in city:
            if address.lower() == c:
                raise serializers.ValidationError('give a place name not city!') 
        return data
        
    


