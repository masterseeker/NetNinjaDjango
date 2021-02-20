from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def article_list(request):

    articles = Article.objects.all().order_by("date")  # fild or column iside the models database
    return render(request, 'articles/article_list.html', {"articles": articles})

def article_detail(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug) # finds article with matching slug
    return render(request, 'articles/article_detail.html', {'article':article})



@login_required(login_url="/accounts/login/")   # decorator protects this view  must be login in to acces this page
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False) # give me the instance before we save it :)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})

