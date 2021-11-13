from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse

from articles.models import Articles

from django.contrib.auth.decorators import login_required

from .forms import ArticleForm
# Create your views here.


def article_search_view(request):

    query_dict = request.GET
    query = query_dict.get("q")  # the name from base.html
    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    articale_obj = None
    if query is not None:
        articale_obj = Articles.objects.get(id=query)

    context = {
        "object": articale_obj,
    }
    return render(request, "articles/search.html", context=context)


#

@login_required
def article_create_view(request):
    # print(request.POST)
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        article_obect = form.save()
        # get what send from browser with name title
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")

        # article_obect = Articles.objects.create(
        # title=title, content=content)
        # print(title, content)
        # context["object"] = article_obect

        # context["created"] = True
        context["form"] = ArticleForm(request.POST or None)
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
#         if form.is_valid():

#             # get what send from browser with name title
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")

#             article_obect = Articles.objects.create(
#                 title=title, content=content)
#             # print(title, content)
#             context["object"] = article_obect

#             context["created"] = True

#     return render(request, "articles/create.html", context=context)


def article_detail_view(request, id=None):
    articale_obj = None
    if id is not None:
        articale_obj = Articles.objects.get(id=id)

    context = {
        "object": articale_obj,
    }
    return render(request, "articles/detail.html", context=context)
