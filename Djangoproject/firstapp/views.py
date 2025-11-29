from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ShoesForm, ClothesForm
from .models import Shoes, Clothes


# Create your views here.
def ourfirstapp(request):
    return HttpResponse("Hello World welcome to our first app")


def home(request):
    # Make root URL show the shoes list
    return redirect('fetchAll')


def createShoes(request):
    form = ShoesForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("fetchAll")
    context = {"form": form}
    return render(request, "forms.html", context)


def createClothes(request):
    form = ClothesForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "forms.html", context)


def fetchAllShoes(request):
    shoes = Shoes.objects.all()
    context = {"shoes": shoes}
    return render(request, "home.html", context)


def shoes_detail(request, pk):
    shoe = get_object_or_404(Shoes, pk=pk)
    return render(request, 'shoes_detail.html', {'shoe': shoe})


def updateShoes(request, pk):
    shoe = get_object_or_404(Shoes, pk=pk)
    form = ShoesForm(request.POST or None, instance=shoe)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('fetchAll')
    return render(request, 'forms.html', {'form': form})


def deleteShoes(request, pk):
    shoe = get_object_or_404(Shoes, pk=pk)
    if request.method == 'POST':
        shoe.delete()
        return redirect('fetchAll')
    return render(request, 'shoes_confirm_delete.html', {'shoe': shoe})


def fetchAllClothes(request):
    clothes = Clothes.objects.all()
    return render(request, 'home.html', {'clothes': clothes})


def clothes_detail(request, pk):
    cloth = get_object_or_404(Clothes, pk=pk)
    return render(request, 'clothes_detail.html', {'cloth': cloth})


def updateClothes(request, pk):
    cloth = get_object_or_404(Clothes, pk=pk)
    form = ClothesForm(request.POST or None, instance=cloth)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'forms.html', {'form': form})


def deleteClothes(request, pk):
    cloth = get_object_or_404(Clothes, pk=pk)
    if request.method == 'POST':
        cloth.delete()
        return redirect('home')
    return render(request, 'clothes_confirm_delete.html', {'cloth': cloth})
