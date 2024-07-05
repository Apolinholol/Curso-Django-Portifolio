from django.shortcuts import render


def home(request):
    return render(request,'recipes/home.html',status=201,context={
        'name':'Matheus'
    })


# Create your views here.
