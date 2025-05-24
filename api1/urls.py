from django.urls import path
from .views import *
urlpatterns = [
    path('student/',StudentView.as_view(),name="student"),
    path('student/update/<int:id>',StudentView.as_view(),name="student"),
    path('student/delete/<int:id>',StudentView.as_view(),name="student"),
]