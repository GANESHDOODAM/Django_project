from views import render
from django.http import HttpResponse, httpResponse

def home(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("This is the about page.")