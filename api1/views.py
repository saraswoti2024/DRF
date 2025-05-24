from django.shortcuts import render,HttpResponse
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.views import Response,APIView
from rest_framework.views import status 

class StudentView(APIView):
    def post(self,request):
        postserializer = StudentSerailzers(data= request.data) #native python
        if postserializer.is_valid():
            postserializer.save() #complex data create if valid
            return Response(postserializer.data,status= status.HTTP_200_OK)
        return Response({'message': postserializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # def get(request,self):
    #     stu = Student.objects.get(id=1)
    #     native = StudentSerailzers(stu)
    #     return Response(native.data)

    def get(self,request):
        stu = Student.objects.all()
        native = StudentSerailzers(stu,many=True)
        return Response(native.data)

    def put(self,request,id):
        stu = Student.objects.get(id=id) #value aayo db bata
        native = StudentSerailzers(stu,data= request.data) #stu old value, data=request.data new value liyo and replace new value 
        if native.is_valid(): #checks new value if it is validated
            native.save() #database ma save, def update ni yeti belai value change garxa in serializers.py ma
            return Response(native.data,status=status.HTTP_200_OK)
        return Response(native.errors,status=status.HTTP_400_BAD_REQUEST)    






