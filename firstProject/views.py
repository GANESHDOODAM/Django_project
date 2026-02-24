from views import render
from django.http import HttpResponse, httpResponse

def home(request):
    return HttpResponse("Hello, World!")