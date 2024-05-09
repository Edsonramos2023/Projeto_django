from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
       'name': 'Edson Ramos' 
    })
    

def recepe(request, id):
    return render(request, 'recipes/pages/home.html', context={
       'name': 'Edson Ramos' 
    })