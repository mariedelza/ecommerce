from typing import Any
from django import http
from django.shortcuts import render,redirect
from store.forms import ArticleForm
from store.models import product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import UpdateView,CreateView,DeleteView

# Create your views here.
def dashboard(request):
    return render(request,'db.html')

@login_required
def user_articles(request):
    has_perm=True
    if request.user.has_perm("store.delete_article"):
        has_perm=True
    list_articles = product.objects.filter()
    return render(request,'my-articles.html',{'list_articles':list_articles ,'has_perm':has_perm})

class AddArticle(LoginRequiredMixin,CreateView):
    model = product
    form_class=ArticleForm
    template_name="add-article.html"
    success_url="my-articles"
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class UpdateArticle(LoginRequiredMixin,UpdateView):
    model = product
    form_class=ArticleForm
    template_name="app_admin/article_form.html" 
    
class DeleteArticle(DeleteView):
    model=product
    success_url="/my-admin/my-articles" 
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("store.delete_article"):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
         
    
    
    
    
    
    
    