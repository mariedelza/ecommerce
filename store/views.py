
from django.shortcuts import render
from .models import product
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.views.generic.edit import UpdateView,CreateView,DeleteView


def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ArticleForm()
    
    return render(request, 'shop/ajouter.html', {'form': form})



def index(request):
    product_object = product.objects.all()
    item_name = request.GET.get('item-name')
    
    if item_name != '' and item_name is not None:
        product_object = product.objects.filter(title__icontains=item_name)
    
    paginator = Paginator(product_object, 100)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    
    return render(request, 'shop/index.html', {'product_object': product_object})

def detail(request, myid):
    product_object=product.objects.get(id=myid)
    return render(request,'shop/detail.html',{'product':product_object})
    
def checkout(request):
    return render(request,'shop/checkout.html')
    