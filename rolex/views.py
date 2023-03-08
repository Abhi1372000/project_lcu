from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dilli(request):
    return HttpResponse("<marquee><h1>Auvnu paer Dilli</h1><marquee>")
def muni(reuest):
    return  HttpResponse("<marquee><h1>Muni is the hottest boy in our Institute, Every girl want to fuck with him</h1><marquee>")