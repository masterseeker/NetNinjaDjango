from django.shortcuts import render
from .models import Article


# Create your views here.
def article_list(request):

    articles = Article.objects.all().order_by("date")  # fild or column iside the models database
    return render(request, 'articles/article_list.html', {"articles": articles})
