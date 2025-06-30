from .models import *
from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) #can only read cannot change
    name = serializers.CharField()
    desc = serializers.CharField()
    active = serializers.BooleanField(read_only=True)

    def create(self,validated_data):
        return Carlist.objects.create(**validated_data)


    #instance-> pahiliko data hunxca ani right side ma  get garda new wala get vayo
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.desc = validated_data.get('desc',instance.desc)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance

    #field level validation -> aauta aauta field ko validation
    def validate_desc(self,value):
        lengths = len(value.strip().split()) ##strip-> aagadi re paxadi ko space hatauxa ani split lae aauta aauta word , gardai split garyo so list ko form ma vayo
        if lengths < 3 :
            raise serializers.ValidationError('at least 10 words should be written!')
        return value
        
    #object level validation -> multiple fields ma validation, single field wala ni garna milyo
    def validate(self,data):
        name = data.get('name')
        desc = data.get('desc')
        desc2 = desc.strip().split()
        for c in desc2:
            if name in c:
                raise serializers.ValidationError('desc and name should not have any common words')
        return data


    