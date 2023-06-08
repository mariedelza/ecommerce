from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    


class Category(models.Model):
    name=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=["-date_added"]
        
    def __str__(self) :
        return self.name    
        
class product(models.Model):
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description =models.TextField()
    category=ForeignKey(Category,related_name="categorie",on_delete=models.CASCADE)
    image=models.CharField(max_length=5000)
    date_added=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=["-date_added"]
        
    def __str__(self) :
        return self.title  
    
    
    
class commande(models.Model):
    items=models.CharField(max_length=300)
    total=models.CharField(max_length=200)
    nom=models.CharField(max_length=200)
    prenom=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,null=False,blank=False)
    address=models.CharField(max_length=200)
    ville=models.CharField(max_length=200)
    pays=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=300)
    date_commande= models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering=['-date_commande']
        
    def __str__(self) :
        return self.prenom 
          
            
    
    
            
        
    
