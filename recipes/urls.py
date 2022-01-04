from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import (
    recipe_list_view,
    recipe_detail_view,
    recipe_delete_view,
    recipe_create_view,
    recipe_list_view_class,
    recipe_update_view,
    recipe_detail_hx_view,
    recipe_ingedient_update_hx_view,
    testCreate,
    shop_view_1,
)


app_name = "recipes"  # recipes:list
urlpatterns = [
    path("", recipe_list_view, name="list"),
    path("create/", recipe_create_view, name="create"),
    path("test/", testCreate.as_view(), name="test"),
    path(
        "hx/<int:parent_id>/ingredient/<int:id>/",
        recipe_ingedient_update_hx_view,
        name="hx-ingredient-detail",
    ),
    path(
        "hx/<int:parent_id>/ingredient/",
        recipe_ingedient_update_hx_view,
        name="hx-ingredient-create",
    ),
    path("hx/<int:id>/", recipe_detail_hx_view, name="hx-detail"),
    path("<int:id>/delete/", recipe_delete_view, name="delete"),
    path("<int:id>/edit/", recipe_update_view, name="update"),
    path("<int:id>/", recipe_detail_view, name="detail"),
    path("list1/", recipe_list_view_class.as_view(), name="list1"),
    path("shop/", shop_view_1, name="shopv"),
]
