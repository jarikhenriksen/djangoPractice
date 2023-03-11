from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addPetForm.html', views.addPets),
    path('addPetSuccess.html', views.addPetSuccess),
    path('<str:name>', views.petPage, name='specificPet'),
    
]
