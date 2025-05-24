from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','roll_no']  ##aagadi admin ma pani list ma dekhauxa value yo garda
    ordering = ['id']