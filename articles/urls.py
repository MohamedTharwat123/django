from django.urls import path

from .views import (
    article_search_view,
    article_create_view,
    article_detail_view,
    article_list_view1,
)


app_name = "articles"  # recipes:list
urlpatterns = [
    path("", article_search_view, name="search"),
    path("create/", article_create_view, name="create"),
    path("<slug:slug>/", article_detail_view, name="detail"),
    path("list/", article_list_view1.as_view(), name="list"),
]
