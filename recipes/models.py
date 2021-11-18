from django.db import models
from django.conf import settings
import pint
from pint import measurement
from django.urls import reverse
from .validators import validate_unit_of_measure
from .utils import number_str_to_float
# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"id": self.id})

    def get_hx_url(self):
        return reverse("recipes:hx-detail", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("recipes:update", kwargs={"id": self.id})

    def get_ingredient_children(self):
        return self.recipeingredient_set.all()


class RecipeIngredient (models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    quanity = models.CharField(max_length=50)
    quantity_as_flaot = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[
                            validate_unit_of_measure])
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

    def covert_to_system(self, system="mks"):
        if self.quantity_as_flaot is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_flaot*ureg[self.unit]
        # print(measurement)
        return measurement  # .to_base_units()

    def to_ounces(self):
        m = self.covert_to_system()
        # print(m)
        return m.to("ounce")

    def as_mks(self):  # meter,kg,second
        measurement = self.covert_to_system(system="mks")
        # print(measurement)
        return measurement.to_base_units()

    def as_imperial(self):  # miles , pounds,seconds
        measurement = self.covert_to_system(system="imperial")
        # print(measurement)
        return measurement.to_base_units()

    def save(self, *args, **kwargs):
        qty = self.quanity
        qty_as_floot, qty_as_floot_success = number_str_to_float(qty)
        if qty_as_floot_success:
            self.quantity_as_flaot = qty_as_floot
        else:
            self.quantity_as_flaot = None
        super().save(*args, **kwargs)

# class RecipeImage():
#     recipe=models.ForeignKey(Recipe)
