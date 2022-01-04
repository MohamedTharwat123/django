from django.shortcuts import render
#
from articles.models import Articles
from recipes.models import Recipe
# Create your views here.

SEARCH_TYPE_MAPPING={
    "article":Articles,
    "articles":Articles,
    "recipe":Recipe,
    "recipes":Recipe 
   

}

def search_view(request):
    query=request.GET.get("q")
    search_type=request.GET.get('type')
    klass=Recipe
    if search_type in SEARCH_TYPE_MAPPING.keys():
        klass=SEARCH_TYPE_MAPPING[search_type]
    qs=klass.objects.search(query=query)
    context={
        'queryset':qs
        
    }
    template="search/results-view.html"
    if request.htmx:
        context['queryset'] = qs[:5]
        
        template="search/partials/results.html"
        
    return render(request,template,context)
    
