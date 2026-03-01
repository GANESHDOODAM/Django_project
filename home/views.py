from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PersonalDetail

# Create your views here.

def home_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")

        PersonalDetail.objects.create(
            name=name,
            email=email,
            age=age
        )
        return redirect('dashboard:dashboard_view')

    return render(request, "home/home.html")

def home_outside(request):
    return HttpResponse("Welcome to the Home Page! of home app")

