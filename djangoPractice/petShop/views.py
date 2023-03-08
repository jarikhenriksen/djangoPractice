from django.shortcuts import render
from django.http import HttpResponse
from petShop.models import Pet



def index(request):

    allPets = Pet.objects.all()
    
    return render(request, 'petShop/index.html', {
        'allPets': allPets
    })


def petPage(request, name):

    specificPet = Pet.objects.get(name = name)
    
    return render(request, 'petShop/specificPet.html', {
        'pet': specificPet
    })

