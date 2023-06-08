from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *

# Create your views here.
def login_blog(request):
   if request.method == "POST":
       form = LoginForm(request.POST)
       if form.is_valid():
           username= form.cleaned_data ['username']
           pwd = form.cleaned_data ['pwd']
           user=authenticate(username=username, password=pwd)
           if user is not None:
               login(request,user)#permet de stocker l'utilisateur dans request
               return redirect("/checkout")
           else:
               messages.error(request, "authentification invalid")
               return render(request,"login.html",{"form":form}) 
       else: 
           return render(request, "login.html", {"form": form})
               
   else:
       form =LoginForm()
       return render(request,'login.html',{"form":form})
   
   
   
def register(request):
    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            pwd=form.cleaned_data ['pwd']
            if(User.objects.filter(username=username).exists()):
                messages.error(request,"Email ou mot de passe incorrect!! veuillez reessayer svp")
                return render(request, "register.html", {"form": form})
            else:
                User.objects.create_user(username=username,password=pwd)
                return redirect("login-blog")
        else:
            return render(request, "register.html", {"form": form})
        return render(request,"register.html",{})
    form = RegisterForm()
    return render(request,"register.html",{"form":form})

def logout_blog(request):
    logout(request)
    return redirect("login-blog")
    

    
    
    
    
    
    
    
    
    
    
      