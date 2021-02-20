"""djangoautic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # allows us to add static files to url patters
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views  # so views are not confused


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('about/', views.about),
    path('', article_views.article_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns() # Need to be in Debug mode for this to work
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
