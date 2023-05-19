from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    


class category(models.Model):
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
    category=ForeignKey(category,related_name="categorie",on_delete=models.CASCADE)
    image=models.CharField(max_length=5000)
    date_added=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=["-date_added"]
        
    def __str__(self) :
        return self.title    
            
    
    
            
        
    
