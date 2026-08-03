from django.shortcuts import redirect, render,HttpResponse
from django.template import context
from .forms import RegisterForm

# Create your views here.
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
    return render(request,"login.html")

def logout_view(request):
    return HttpResponse("Logout")

def delete_task(request,id):
    return HttpResponse("delete") 