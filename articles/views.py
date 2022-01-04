from django.db.models import lookups, query
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic.list import ListView
from articles.models import Articles
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .forms import ArticleForm
from .models import Articles

# Create your views here.


def article_search_view(request):

    query = request.GET.get("q")  # the name from base.html
    print(request.GET.get("q"))
    qs = Articles.objects.search(query=query)

    context = {
        "object_list": qs,
    }
    print(context)
    return render(request, "articles/search.html", context=context)


#


@login_required
def article_create_view(request):
    # print(request.POST)
    form = ArticleForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        article_object = form.save()
        # get what send from browser with name title
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")

        # article_obect = Articles.objects.create(
        # title=title, content=content)
        # print(title, content)
        # context["object"] = article_obect

        # context["created"] = True
        context["form"] = ArticleForm(request.POST or None)
        return redirect(article_object.get_absolute_url())
    return render(request, "articles/create.html", context=context)


# def article_create_view(request):
#     # print(request.POST)
#     form = ArticleForm()
#     context = {
#         "form": form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         context["form"] = form
#         if form.is_valid():            #function

#             # get what send from browser with name title
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")

#             article_obect = Articles.objects.create(
#                 title=title, content=content)
#             # print(title, content)
#             context["object"] = article_obect

#             context["created"] = True

#     return render(request, "articles/create.html", context=context)


def article_detail_view(request, slug=None):
    articale_obj = None
    print(request)
    print(slug)
    if slug is not None:
        try:
            articale_obj = Articles.objects.get(slug=slug)
        except:
            Http404

    context = {
        "object": articale_obj,
    }
    return render(request, "articles/detail.html", context=context)


class article_list_view1(ListView):
    model = Articles
    fields = ["all"]
