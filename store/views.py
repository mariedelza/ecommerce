
from django.shortcuts import render, get_object_or_404
from .models import product,commande
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Category,product
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
    if request.method=="POST":
        items=request.POST.get('items')
        total=request.POST.get('total')
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        email=request.POST.get('email')
        address=request.POST.get('address')
        ville=request.POST.get('ville')
        pays=request.POST.get('pays')
        zipcode=request.POST.get('zipcode')
        com=commande(items=items,total=total,nom=nom,prenom=prenom,email=email,address=address,ville=ville,pays=pays,zipcode=zipcode)
        com.save()
        return redirect('confirmation')
        
    
    return render(request,'shop/checkout.html')

def confirmation (request):
    info=commande.objects.all()[:1]
    for item in info:
        nom=item.nom
        prenom=item.prenom
    
    
    return render(request,'shop/confirmation.html',{'name':nom,'prenom':prenom})
        

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})        
        
        
        
        

def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = product.objects.filter(category=category)
    return render(request, 'shop/product_list.html', {'category': category, 'products': products})
        
def contact(request):
    return render(request,'contact.html')        