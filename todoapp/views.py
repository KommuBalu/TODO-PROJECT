from django.http import request
from django.shortcuts import redirect, render,HttpResponse
from django.template import context
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def home(request):
    return render(request,"index.html")


def register_view(request):

    if request.method == "POST":
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request,"register.html",{'form': form})




def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")   # lowercase — must match urls.py name
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")



@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

def delete_task(request,id):
    return HttpResponse("delete") 