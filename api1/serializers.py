from rest_framework import serializers
from .models import *

class StudentSerailzers(serializers.ModelSerializer):

    ##validators -> tyo field matra liyere bahirw define garne for meta(modelserializer), for normal serializers tahi normally sabai field lekhnu paryo ani garnu paryo
    def chare(value):
        if value is not None:
            for c in value:
                if c.isupper():
                    raise serializers.ValidationError("it should be in lower case")
        return value

    name = serializers.CharField(max_length=100, validators = [chare])
    class Meta:
        model = Student
        fields = '__all__'
    
    ##field level validation
    def validate_roll_no(self,value):
        if value>200:
            raise serializers.ValidationError('seat Full')
        # if Student.objects.filter(roll_no=value).exists():
        #     raise serializers.ValidationError('already exists, use another number less than 200')
        return value
      
    ##object level validation
    def validate(self,data):
        address = data.get('address')
        city = ['kathmandu','bhaktapur','biratnagar','lalitpur','hetauda']
        if address is not None:
            for c in city:
                if address.lower() == c:
                    raise serializers.ValidationError('give a place name not city!') 
        return data
        
    


