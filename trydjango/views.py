"""
    To render html web pages
"""
from django.http import HttpResponse

from articles.models import Article
from django.template.loader import render_to_string

import random

HTML_STRING ="""
<h1>Hello World</h1>
"""


def home_view(request):
    """
    To take in a request (Django sends request )
    Returns HTMl as response (We pick to return response)
    """
    random_id = random.randint(1,3)
    
    
    article_obj = Article.objects.get(id=random_id)
    
    article_queryset = Article.objects.all()
    
    
    context = {
        "object_list":article_queryset,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }
    
    # Django Templates
    HTML_STRING =render_to_string('home-view.html', context=context)
    
    # HTML_STRING = f"""
    # <h1>{title} (id = {id}!)</h1>
    # <p>{content} (id = {id}!)</p>
    # """.format(**context)
    
    
    return HttpResponse(HTML_STRING)