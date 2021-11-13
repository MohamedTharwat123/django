"""
render html web pages
"""
from django.http import HttpResponse


html_string = """
<h1>Hello World</h>
"""


def home_view(request):
    """
    take in request(django send request)    
    return html as response(we pick to return the response)
    """
    return HttpResponse(html_string)
