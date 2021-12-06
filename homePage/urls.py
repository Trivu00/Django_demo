from django.conf.urls import url
from django.urls.conf import path

from django.views.generic.base import RedirectView
from . import views 

app_name = 'homePage'
urlpatterns = [ 
    path('homepage/', views.homePage, name='homePage'),
    path(r'', RedirectView.as_view(url='homepage/', permanent=False), name='homePageDefault'), # tự động trỏ đến homepage nếu url để trống
    path('reading/', views.readingSite, name='readingSite'),
    path('readpage/<int:id>/', views.readPageSite, name='readPageSite'),
    path('post/', views.post, name='post'),
    path('note-book/', views.notebook, name='note-book') 
]