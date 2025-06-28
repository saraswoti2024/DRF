from django.shortcuts import render
from .models import *
from django.http import JsonResponse,HttpResponse
import json
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

######################################JSONREsponse#########################################
# def car_list(request):
#     cars = Carlist.objects.all() 
#     data = {
#         'cars' :list(cars.values()) 
#     }
#     return JsonResponse(data)

#     #using httpresponse
#     # data_json = json.dumps(data)
#     # return HttpResponse(data_json,content_type = 'application/json')

# def car_list_detail(request,id):
#     car = Carlist.objects.get(id=id)
#     data = {
#        'name' : car.name,
#        'desc' : car.desc,
#        'active' : car.active,
#     }
#     return JsonResponse(data)

#####################################jsonresponseend###########################################


# ------------------------------------------serializers----------------------------------------#
#------------1.@api_view-------------

#if no request send then by default get request
@api_view(['GET','POST'])
def car_list(request):
    if request.method == 'GET':
        car = Carlist.objects.all()
        serializer = CarSerializer(car,many=True)
        return Response(serializer.data) 
    
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','PUT','PATCH','DELETE'])
def car_list_detail(request,id):
    if request.method == 'GET':
        car = Carlist.objects.get(id=id)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT': 
        car = Carlist.objects.get(id=id) #database
        serializer = CarSerializer(car,data = request.data)  #complex data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == 'PATCH': 
        car = Carlist.objects.get(id=id) #database
        serializer = CarSerializer(car,data = request.data,partial=True)  #complex data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        car = Carlist.objects.get(id=id)
        car.delete()
        return Response({'message': 'deleted'})
    
#----------api view ended----------