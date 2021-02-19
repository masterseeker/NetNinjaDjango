from django.urls import path
from . import views

app_name = 'accounts' # allows us to name space a url file so its uniqe
                    # allows us to avoid collison by stating the urls file
                    # articles:detail instead of the name just detail

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout")

]



