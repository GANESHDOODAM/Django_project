from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('home_outside/', views.home_outside, name='home_outside'),

]