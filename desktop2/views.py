from django.shortcuts import render
from .models import Carlist
from django.http import JsonResponse

def car_list(request):
    cars = Carlist.objects.all() 
    data = {
        'cars' :list(cars.values()) 
    }
    return JsonResponse(data)

def car_list_detail(request,id):
    car = Carlist.objects.get(id=id)
    data = {
       'name' : car.name,
       'desc' : car.desc,
       'active' : car.active,
    }
    return JsonResponse(data)