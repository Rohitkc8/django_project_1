from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
def Login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("/admin/")  
            else:
                return redirect("/inventory/project/")

        else:
            return render(request, "login_page.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login_page.html")
def Logout_user(request):
    logout(request)

    return redirect("/")

def Signup_user(request):
        
        if request.method=="POST":
             
             new_user= User(username=request.POST['username'],password=request.POST['password'],first_name=request.POST['firstname'],last_name=request.POST['lastname'])
             new_user.save()
        return render(request,"signup_page.html")