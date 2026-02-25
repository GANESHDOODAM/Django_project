from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World! this is from project views , url ` ` ")

def about(request):
    return HttpResponse("This is the about page.this is from project views , url `about\` ")