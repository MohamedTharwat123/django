"""
render html web pages
"""
from django import http
from django.http import HttpResponse
import random

from articles.models import Articles

from django.template.loader import render_to_string


def home_view(request, id=None):
    """
    take in request(django send request)    
    return html as response(we pick to return the response)
    """
    name = "mohamed"
    num = random.randint(1, 40)
    # print(kwarags, args)
    # get data from db
    art_obj = Articles.objects.get(id=num)
    articale_queryset = Articles.objects.all()

    context1 = {
        "object_list": articale_queryset,
        "title": art_obj.title,
        "id": art_obj.id,
        "content": art_obj.content

    }

    # django templates
    html_string = render_to_string("home-view.html", context=context1)
    # html_string = """
    # <h1>{title} (id:{id})</h1>
    # <p>{content}</p>
    # """.format(**context1)

    return HttpResponse(html_string)
