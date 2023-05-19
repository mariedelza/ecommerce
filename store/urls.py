from django.urls import path
from store.views import index,detail,checkout
from . import views


urlpatterns = [
    path('',index, name="home"),
     path('ajouter/', views.ajouter_article, name='ajouter'),
    path('<int:myid>', detail,name="detail"),
    path('checkout', checkout,name="checkout")
]


