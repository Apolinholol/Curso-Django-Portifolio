# estou importando da pasta from recipes.views import home, usando o 'ponto'
from . import views
from django.urls import path

app_name='recipes'

urlpatterns = [

    path('',views.home,name="home"),#home
    # Id sera enviado como parametro para recipe
    # tag <int:id> foi usada para permitir apenas numeros após a barra para melhorar a segurança da url
    path('recipes/<int:id>/',views.recipe,name="recipe"),
    # Será linkado ao botão em recipe da categoria da receita
    path('recipes/category/<int:category_id>/',views.category,name="category"),
   
]