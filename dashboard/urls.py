from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:person_id>/', views.edit, name='edit'),
    path('delete/<int:person_id>/', views.delete, name='delete'),
]
