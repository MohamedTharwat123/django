from django.contrib.admin.decorators import action
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from pint import test
from .forms import RecipeForm, RecipeIngredientForm
from .models import Recipe, RecipeIngredient, test, ShopItems
from django.forms.models import ModelForm, modelformset_factory
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)

    context = {"object_list": qs}
    return render(request, "recipes/list.html", context)


@method_decorator(login_required, name="dispatch")
class recipe_list_view_class(ListView):
    model = Recipe

    template_name = "recipes/list.html"
    context_object_name = "object_list"


@login_required
def recipe_detail_view(request, id=None):
    hx_url = reverse("recipes:hx-detail", kwargs={"id": id})
    context = {"hx_url": hx_url}
    return render(request, "recipes/detail.html", context)


@login_required
def recipe_detail_hx_view(request, id=None):
    if not request.htmx:
        raise Http404
    try:
        obj = Recipe.objects.get(id=id, user=request.user)
    except:
        obj = None

    if obj is None:
        return HttpResponse("Not Found. ")

    context = {"object": obj}
    return render(request, "recipes/partials/detail.html", context)


@login_required
def recipe_create_view(request, id=None):
    form = RecipeForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())
    return render(request, "recipes/create-update.html", context)


class testCreate(LoginRequiredMixin, CreateView):
    model = test
    fields = ["id", "test"]

    success_url = reverse_lazy("recipes:test")


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    new_ingredient_url = reverse(
        "recipes:hx-ingredient-create", kwargs={"parent_id": obj.id}
    )

    context = {"form": form, "object": obj, "new_ingredient_url": new_ingredient_url}

    if form.is_valid():
        form.save()
        context["message"] = "Data Saved"

    if request.htmx:
        return render(request, "recipes/partials/forms.html", context)
    return render(request, "recipes/create-update.html", context)


@login_required
def recipe_ingedient_update_hx_view(request, parent_id=None, id=None):
    if not request.htmx:
        raise Http404
    try:
        parent_obj = Recipe.objects.get(id=parent_id, user=request.user)
    except:
        parent_obj = None

    if parent_obj is None:
        return HttpResponse("Not Found. ")

    instance = None
    if id is not None:

        try:
            instance = RecipeIngredient.objects.get(recipe=parent_obj, id=id)
        except:
            instance = None
    form = RecipeIngredientForm(request.POST or None, instance=instance)
    url = reverse("recipes:hx-ingredient-create", kwargs={"parent_id": parent_obj.id})

    if instance:
        url = instance.get_hx_edit_url()
    context = {"url": url, "form": form, "object": instance}

    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.recipe = parent_obj
        new_obj.save()
        context["object"] = new_obj
        return render(request, "recipes/partials/ingredient-inline.html", context)

    return render(request, "recipes/partials/ingredient-form.html", context)


def shop_view_1(request):
    qs = ShopItems.objects.all()
    print("*" * 50)

    context = {
        "object_list": qs,
    }

    return render(request, "accounts/shop.html", context=context)
