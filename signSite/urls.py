from django.conf.urls import url
from django.contrib.auth import views as auth_views
from usefulModels.getIdiom import getIdiom

from . import views 

app_name = 'signSite'
urlpatterns = [ 
    url('signup/', views.signUp, name='signUp'),
    url('signin/', auth_views.LoginView.as_view(template_name='signIn.html', extra_context={'title': 'Sign In', 'idiom4Day': getIdiom()}), name='signIn'),
    url('signout/', auth_views.LogoutView.as_view(template_name='signOut.html', extra_context={'title': 'Sign Out', 'idiom4Day': getIdiom()}), name='signOut'),
]