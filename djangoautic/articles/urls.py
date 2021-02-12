from django.urls import path
from . import views 

app_name='articles' # allows us to name space a url file so its uniqe
                    # allows us to avoid collison by stating the urls file
                    # articles:detail instead of the name just detail

urlpatterns = [
    path('', views.article_list, name="list"),
    path('<slug:slug>/', views.article_detail, name="detail"),

]



