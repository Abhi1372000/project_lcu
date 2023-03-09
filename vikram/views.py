from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_vik(request):
    return HttpResponse('Hi good morning, The eagle is comming')