from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import RecipeIngredient, Recipe
from django.core.exceptions import ValidationError
# Create your tests here.
from .utils import number_str_to_float
user = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = user.objects.create_user('test', password='abc123')
        self.recipe_a = Recipe.objects.create(
            name="grilled chicked", user=self.user_a)

    def test_user_pw(self):
        checked = self.user_a.check_password('abc123')
        self.assertTrue(checked)


class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = user.objects.create_user('test', password='abc123')

        self.recipe_a = Recipe.objects.create(
            name="grilled chicked", user=self.user_a)
        self.recipe_b = Recipe.objects.create(
            name="grilled chicked taco", user=self.user_a)

        self.recipe_ingredient_a = RecipeIngredient.objects.create(
            recipe=self.recipe_a, name="chicken", quanity="1/2", unit="pound")

        self.recipe_ingredient_b = RecipeIngredient.objects.create(
            recipe=self.recipe_a, name="chicken", quanity="asdasd", unit="pound")

    def test_user_count(self):
        qs = user.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reversed_count(self):
        user = self.user_a
        qs = user.recipe_set.all()

        self.assertEqual(qs.count(), 2)

    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)

        self.assertEqual(qs.count(), 2)

    def test_user_recipe_ingredient_reversed_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()

        self.assertEqual(qs.count(), 2)

    def test_user_recipe_ingredient_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)

        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation_reverse(self):
        user = self.user_a
        RecipeIngredient_ids = list(user.recipe_set.all(
        ).values_list("recipeingredient__id", flat=True))
        qs = RecipeIngredient.objects.filter(id__in=RecipeIngredient_ids)
        print(RecipeIngredient_ids)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation_via_recipes(self):
        user = self.user_a
        ids = user.recipe_set.all().values_list("id", flat=True)
        qs = RecipeIngredient.objects.filter(recipe__id__in=ids)
        self.assertEqual(qs.count(), 2)

    def test_unit_measure_validation(self):
        invalid_unit = 'ounce'
        ingredient = RecipeIngredient(
            name='New',
            quanity=10,
            recipe=self.recipe_a,
            unit=invalid_unit
        )
        ingredient.full_clean()

    def test_unit_measure_validation_error(self):
        invalid_units = ['nada', 'asdfadsf']
        with self.assertRaises(ValidationError):
            for unit in invalid_units:
                ingredient = RecipeIngredient(
                    name='New',
                    quanity=10,
                    recipe=self.recipe_a,
                    unit=unit
                )
                ingredient.full_clean()

    def test_quintaty_as_float(self):
        self.assertIsNotNone(self.recipe_ingredient_a.quantity_as_flaot)
        self.assertIsNone(self.recipe_ingredient_b.quantity_as_flaot)
