from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home, name='home'),
    path('home_outside/', views.home_outside, name='home_outside'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
]