from django.db import models
from django.conf import settings
import pint
from pint import measurement
from django.urls import reverse
from .validators import validate_unit_of_measure
from .utils import number_str_to_float

import pathlib
import uuid

from django.db.models import Q

# Create your models here.


user = settings.AUTH_USER_MODEL


class RecipeQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = (
            Q(name__icontains=query)
            | Q(description__icontains=query)
            | Q(directions__icontains=query)
        )
        return self.filter(lookups)


# new
class RecipeManger(models.Manager):
    def get_queryset(self):
        return RecipeQuerySet(self.model, using=self._db)

    def search(self, query=None):

        return self.get_queryset().search(query=query)


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = RecipeManger()

    @property
    def title(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"id": self.id})

    def get_hx_url(self):
        return reverse("recipes:hx-detail", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("recipes:update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("recipes:delete", kwargs={"id": self.id})

    def get_ingredient_children(self):
        return self.recipeingredient_set.all()


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    quanity = models.CharField(max_length=50)
    quantity_as_flaot = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

    def get_hx_edit_url(self):
        kwargs = {"parent_id": self.recipe.id, "id": self.id}
        return reverse("recipes:hx-ingredient-detail", kwargs=kwargs)

    def covert_to_system(self, system="mks"):
        if self.quantity_as_flaot is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_flaot * ureg[self.unit]
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


class test(models.Model):
    id = models.IntegerField(primary_key=True)

    test = models.TextField(blank=True, null=True)


# class RecipeImage():
#     recipe=models.ForeignKey(Recipe)


def shop_image(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())  # uuid + timestamps
    return f"{new_fname}{fpath.suffix}"


class ShopItems(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=shop_image)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(
        max_digits=2, decimal_places=0, blank=True, null=True
    )

    @property
    def auto_cal(self):
        a = self.price * (1 - (self.discount / 100))
        x = "%.2f" % a
        return x
