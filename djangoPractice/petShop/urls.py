from django.urls import path, include, reverse
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:name>', views.petPage, name='specificPet'),
    
]
