from django.urls import path
from .views import *

urlpatterns = [
    path('list',car_list,name="list"),
    path('list/<int:id>',car_list_detail,name="list_detail"),
]