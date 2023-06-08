from django.contrib import admin
from .models import Category,product,commande

# Register your models here.
admin.site.site_header="E-commerce"
admin.site.site_title="Marie Ndiaye"
admin.site.index_title="Marie Ndiaye"

class AdminCategorie(admin.ModelAdmin):
    list_display=('name','date_added')
    
class AdminProduct(admin.ModelAdmin):
    list_display=('title','price','category','date_added')
    search_fields=('title',)
    list_editable=('price',)
class Admincommande(admin .ModelAdmin):
    list_display=('items','nom','prenom','email','address','ville','pays','total','date_commande')        


admin.site.register(product,AdminProduct)
admin.site.register(Category,AdminCategorie)
admin.site.register(commande,Admincommande)

