from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse


# Create your views here.
def article_list(request):

    articles = Article.objects.all().order_by("date")  # fild or column iside the models database
    return render(request, 'articles/article_list.html', {"articles": articles})

def article_detail(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug) # finds article with matching slug
    return render(request, 'articles/article_detail.html', {'article':article})

    

