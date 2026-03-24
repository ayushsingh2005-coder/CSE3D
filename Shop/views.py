from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Contact
# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        msg=request.POST.get("msg")

        c = Contact(name=name,email=email,phone=phone,msg=msg)
        c.save()
    data = Contact.objects.all()
        
    return render(request,'contact.html',{"data":data})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            return render(request,'index.html',{"username":username})
        else:
            redirect('/login')
            # No backend authenticated the credentials
    return render(request,'login.html')
def signup(request):
    if request.method =="POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        if(password==cpassword):
            user = User.objects.create_user(name, email, password)
            user.save()
            return redirect('/login')
        else:
            return render(request,'signup.html',{'error':'password  and confirm password are not matching'})
    return render(request,'signup.html')

def logout_view(request):
    logout(request)
    return redirect('/login')