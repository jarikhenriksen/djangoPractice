from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from petShop.models import Pet

from .forms import PetForm

def index(request):

    allPets = Pet.objects.all()

    return render(request, 'petShop/index.html', {
        'allPets': allPets,
        
    })


def petPage(request, name):

    specificPet = Pet.objects.get(name = name)
    
    return render(request, 'petShop/specificPet.html', {
        'pet': specificPet
    })

def addPets(request):

    if request.method == 'POST':
            form = PetForm(request.POST)

            if form.is_valid():
                HttpResponseRedirect('/')

    else:
        form = PetForm()

    return render(request, 'petShop/index.html', {
        'form': form
    })