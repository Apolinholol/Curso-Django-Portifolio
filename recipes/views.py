from django.shortcuts import render,get_list_or_404,get_object_or_404
from utils.recipes.factory import make_recipe
from .models import Recipe
from django.http import Http404
from django.contrib import messages 



def home(request):
    #Comandos do DJANGO pegar todos os objetos e ordenar por id
    recipes=Recipe.objects.filter(is_published=True).order_by('-id')
    #caminho onde se encontra a home
    return render(request,'recipes/pages/home.html',status=201,context={
        # importando de factory e linkando com urls de recipes para exibir na home
        'recipes':recipes,
    })

def category(request,category_id):
    
    # #Comandos do DJANGO filter usando uma chave estrangeira em Recipes.models para acessar Category também 
    # # em models.Category
    # recipes=Recipe.objects.filter(category__id=category_id,is_published=True).order_by('-id')
    # #caminho onde se encontra a home


    # if not recipes:
    #    raise Http404('Not found😥')

    recipes= get_list_or_404(Recipe.objects.filter(category__id=category_id
                                                   ,is_published=True)
                                                   )

    return render(request,'recipes/pages/category.html',status=201,context={
         # importando de factory.py e linkando com urls.pu de recipes para exibir na home
        'recipes':recipes,
        'title':f'{recipes[0].category.name} - Category |'
        # Pega o nome da categoria que a receita está usando
    })


def recipe(request, id):       
                                    #ou pk=id
    # recipe=Recipe.objects.filter(id=id,is_published=True
    #                              ).order_by('-id').first()
    recipes=get_object_or_404(Recipe,id=id,is_published=True) 

                         #caminho onde se encontra a home
    return render(request,'recipes/pages/recipe-view.html',status=201,context={
        'recipe': recipes,
        'is_detail_page':True,
    })

def search(request):
   search_term=request.GET.get('search')

   if not search_term:
       raise Http404()
   
   return render(request,'recipes/pages/search.html') 


# recipes=Recipe.objects.filter(category__id=category_id,is_published=True).order_by('-id')