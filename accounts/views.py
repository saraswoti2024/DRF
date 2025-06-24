from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from django.contrib.auth.models import User
# Create your views here.


class Register(APIView):
    def post(self,request):
        try:
            serializer = RegistrationSerializer(data=request.data) #native python
            if serializer.is_valid(): #validation check
                serializer.save() #databse save
                return Response({'message': 'user registered successfully!'},status=status.HTTP_201_CREATED)
            return Response({'message1':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message_exception':f'{str(e)}'},status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request):
        try:
            data = User.objects.all()
            datas = RegistrationSerializer(data,many=True)
            return Response(datas.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message_exception':f'{str(e)}'},status=status.HTTP_404_NOT_FOUND)
        
            