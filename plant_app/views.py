from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from . models import *
from adminapp.models import *

# Create your views here.
def index(request): 
    data=Addb.objects.all()
    return render(request, "index.html", {'data':data})

def register(request):
    return render(request, "register.html")

def getdata(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phn=request.POST.get('phn')
        address=request.POST.get('address')
        password=request.POST.get('password')
        data=Registerdb(name=name,email=email,phn=phn,address=address,password=password)
        data.save()
        return redirect("index")
        
def viewdata(request):
    data=Registerdb.objects.all()
    return render(request, "viewdata.html", {'data': data})

def contact(request):
    return render(request,"contact.html")

def login(request):
    return render(request,"login.html")

def getlogin(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        if Registerdb.objects.filter(email=email,password=password).exists():
            return redirect("loginhome")
        else:
            return render(request, "login.html", {'msg': 'Invalid User Credentials'})
    else:
        return redirect('index')

def booking(request):
    data=Plantdb.objects.all()
    return render(request, "booking.html", {'data': data})

def getvalue(request):
    if request.method == "POST":
        pname=request.POST.get('pname')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        plants=request.POST.get('plants')
        data=Bookingdb(pname=pname,phone=phone,address=address,plants=plants)
        data.save()
        return redirect("loginhome")

def loginhome(request):
    return render(request, "loginhome.html")

def logout(request):
    auth.logout(request)
    return redirect("index")

def addplant(request):
    return render(request, "addplant.html")


def getplant(request):
    if request.method == "POST":
        plant_image=request.FILES['plant_image']
        plantname=request.POST.get('plantname')
        description=request.POST.get('description')
        data=Addb( plant_image=plant_image,plantname=plantname,description=description)
        data.save()
        return redirect("addplant")

def edit(request, did):
    data=Registerdb.objects.filter(id=did)
    return render(request, "edit.html", {'data': data})

def update(request, did):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phn=request.POST.get('phn')
        address=request.POST.get('address')
        password=request.POST.get('password')
        
        Registerdb.objects.filter(id=did).update(name=name,email=email,phn=phn,address=address,password=password)
        return redirect("viewdata")

def delete(request, did):
    Registerdb.objects.filter(id=did).delete()
    return redirect("viewdata")
        
def viewplant(request):
    data=Addb.objects.all()
    return render(request, "viewplant.html", {'data': data}) 

def view(request,did):
    data=Addb.objects.filter(id=did)
    return render(request, "view.html", {'data': data}) 

def viewbook(request):
    data=Bookingdb.objects.all()
    return render(request, "viewbook.html", {'data':data})