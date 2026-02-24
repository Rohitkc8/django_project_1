from django.shortcuts import render,redirect
from .forms import *
from .models import *

def HomePage(request):
     return render(request,'home.html')
def navbarPage(request):
     return render(request,'navbar.html')
def contactPage(request):
     return render(request,'contact.html')
def homePage(request):
     return render(request,'home.html')
def servicePage(request):
     return render(request,'service.html')
def aboutPage(request):
     return render(request,'about.html')
def projectPage(request):
     return render(request,'project.html')
def products_add(request):
     context ={
          'product_form': Product_Form()
     }
          
     if request.method=="POST":

          product_form =Product_Form(request.POST)

          if product_form.is_valid():
               product_form.save()
          
     return render(request,'products_add.html',context)

def All_products(request):
    
     context={
          "all_products":product.objects.all()
     }
     return render(request,'products.html',context)

def Delete_Product(request, id):
     selected_product= product.objects.get(id=id)

     selected_product.delete()
     return redirect('/inventory/products/')

def Update_Product(request,id):
     selected_product= product.objects.get(id=id)

     context={
          "product_form":Product_Form(instance=selected_product)
     }

     if request.method=="POST":
          product_form =Product_Form(request.POST,instance=selected_product)

          if product_form.is_valid():
               product_form.save()

          return redirect('/inventory/products/')
     return render(request,'products_add.html',context)