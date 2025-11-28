from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ourfirstapp(request):
    return HttpResponse("This is our first app in Django")