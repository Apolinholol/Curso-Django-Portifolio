from django.db import models
# User é uma tabela na base de dados
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=65)
    # Para tornar visível os nomes das receitas na aba de admins
    def __str__(self) :
        
        return self.name
            


# a classe Recipe seria tabela da base de dados por conta de Model
class Recipe(models.Model):
    title = models.CharField(max_length=65) #equivale à um varchar do SQL
    description = models.CharField(max_length=165)
#Slugs são usados ​​principalmente para criar URLs amigáveis e legíveis. Eles normalmente consistem em letras minúsculas, 
# números e hifens, evitando caracteres especiais e espaços.
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length= 30)
    servings= models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html= models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published= models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d',blank=True, default='')
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True,blank=True,default=None)
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)

    # retornando o título da receita
    def __str__(self):
            return self.title