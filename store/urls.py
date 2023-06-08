from django.urls import path
from store.views import index,detail,checkout,confirmation,category_list, product_list,contact
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',index, name="home"),
     path('ajouter/', views.ajouter_article, name='ajouter'),
    path('<int:myid>', detail,name="detail"),
    path('checkout', checkout,name="checkout"),
     path('contact', contact,name="contact"),
    path('confirmation', confirmation, name="confirmation"),
     path('categories/', category_list, name='category_list'),
    path('products/<int:category_id>/', product_list, name='product_list'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


