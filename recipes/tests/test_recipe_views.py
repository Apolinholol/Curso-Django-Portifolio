
from django.urls import reverse,resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


# @skip("Pulando a classe de testes RecipeViewsTest")
class RecipeViewsTest(RecipeTestBase):
    # Verifica as URLs para quais funções elas estão renderizando nos templates em views
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home')) 
        self.assertIs(view.func,views.home)#verificando se as funções apontam para o mesmo lugar

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 201)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        # Recipe.objects.get(pk=1).delete() forçando que o teste passe através de um setup e teardown
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here 😥</h1>',
            response.content.decode('utf-8')
        )
    
  
    def test_recipe_home_templates_loads_recipes(self):
        # category=Category(name='Categoria')
        # category.full_clean()
        # category.save() mesma coisa que o abaixo
        
        # Need a recipe for this test
        self.make_recipe()

        # Pegando o contexto(informações) diretamente da view, de dentro para fora 
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        # Check if one recipe exists
        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)
    
    def test_recipe_home_templates_dont_load_recipe_not_published(self):
        # Need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        # Garantindo que o id da receita não será de uma existente
        response = self.client.get(reverse('recipes:recipe', kwargs={'id':recipe.category.id}))
        
        self.assertEqual(response.status_code,404)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        # Need a recipe for this test
        self.make_recipe(title1=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        # Check if one recipe exists
        self.assertIn(needed_title, content)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a detail page - It load one recipe'

        # Need a recipe for this test
        self.make_recipe(title1=needed_title)

        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': 1
                }
            )
        )
        content = response.content.decode('utf-8')

        # Check if one recipe exists
        self.assertIn(needed_title, content)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
        self.fail() #Forçando o teste a falhar
    
    def test_recipe_detail_templates_dont_load_recipe_recipes_not_published(self):
        # Need a recipe for this test
        recipe = self.make_recipe(is_published1=False)

        # Garantindo que o id da receita não será de uma existente e criada por um usuario
        response = self.client.get(reverse('recipes:recipe', kwargs={'id':recipe.id}))
        
        self.assertEqual(response.status_code,404)

    def test_recipe_search_uses_correct_view_function(self):
        resolved= resolve(reverse('recipes:search'))
        self.assertIs(resolved.func,views.search)
    
    def test_recipe_search_loads_correct_template(self):
        response=self.client.get(reverse('recipes:search'))
        self.assertTemplateUsed(response,'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        url=reverse('recipes:search') 
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)