from .test_recipe_base import RecipeTestBase, Recipe
from parameterized import parameterized
from django.core.exceptions import ValidationError

class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name='Test Default Category'),
            author=self.make_author(username='newuser'),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def test_the_test(self):
        recipe = self.recipe
        ...
        # .expand por estar dentro de uma classe
   

    def test_recipe_title_error_more_65_char(self):
        
        self.recipe.title =  'a' * 70

# Levantará um erro especifico e caso não levante, o teste falhará, pois se espera nesse caso  estourarar o limite de 65 chars
        with self.assertRaises(ValidationError):
            self.recipe.full_clean() #Aqui o ocorre a validação caso estoure o limite de caracterers


        # self.recipe.save() # Salva na base de dados e se estivesse sem o full clean, salvaria independente de dar erro ou nao
        # self.fail(self.recipe.title)


    # .expand por estar dentro de uma classe
    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])

    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1)) # setattr tem as mesma função que 'self.recipe.title =', porém é dinâmico
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparation_steps_is_html is not False',
        )
    
    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is_published is not False',
        )
    
   
