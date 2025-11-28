from django.shortcuts import render, redirect
from .forms import ShoesForm
from .models import Shoes




# Create your views here.
def ourfirstapp(request):
    return HttpResponse("Hello World welcome to our first app")
 
def home(request):
    return render(request, 'home.html')

def createShoes(request):
    form=ShoesForm()
    
    if request.method=="POST":
        form=ShoesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("fetchAll")
    context={"form":form}         
    return render(request, "forms.html",context)

def createClothes(request):
    form=ClothesForm()
    context={"form":form}
    if request.method=="POST":
        form=ClothesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
             
        
    return render(request, "forms.html",context)

def fetchAllShoes(request):
    shoes=Shoes.objects.all()
    print(f"==>{shoes}")
    context={"shoes":shoes}
    return render(request,"home.html" , context)
