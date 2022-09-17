from django.shortcuts import render
from . models import Deals

# Create your views here.

def index(request):
    obj=Deals.objects.all()

    return render(request,'index.html',{'result': obj})

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')