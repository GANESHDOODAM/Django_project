from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home1(request):
    return HttpResponse("Welcome to the Home Page! of home app")

def page1(request):
    return HttpResponse("This is Page 1 of home app")

def page2(request):
    return HttpResponse("This is Page 2 of home app")