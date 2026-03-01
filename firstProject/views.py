from django.shortcuts import render
from django.http import HttpResponse

def main_page(request):
    return render(request, 'project/base.html')

def about(request):
    return HttpResponse("This is the about page - HOME PAGE - PROJECT FOLDER, url `about\` ")

