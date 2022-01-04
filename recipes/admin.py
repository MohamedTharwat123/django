from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models.base import Model

# Register your models here.
from .models import Recipe, RecipeIngredient, ShopItems


admin.site.register(ShopItems)
User = get_user_model()


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    readonly_fields = ["quantity_as_flaot", "as_mks", "as_imperial", "to_ounces"]
    # fields = ['name', 'quanity', 'unit', 'directions']


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ["name", "user"]
    readonly_fields = ["timestamp", "updated"]
    raw_id_fields = ["user"]


admin.site.register(Recipe, RecipeAdmin)
