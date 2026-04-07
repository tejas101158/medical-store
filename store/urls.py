from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rental/', views.rental, name='rental'),
    path('surgical/', views.surgical, name='surgical'),
]