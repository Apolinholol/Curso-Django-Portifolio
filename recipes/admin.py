from django.contrib import admin
#Será usado para funções de admin no site
from .models import Category,Recipe

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin (admin.ModelAdmin):
    ...

# Foi colocado na aba abaixo de usuarios e users em /admin
admin.site.register(Category,CategoryAdmin)
