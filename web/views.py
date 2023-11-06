from django.shortcuts import render
from .models import courses,courses1,courseCategory
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import form

# Create your views here.


def about(request):
    return render(request,'web/about.html')
def blog(request):
    return render(request,'web/blog.html')
def blogsingle(request):
    return render(request,'web/blog-single.html')
def course(request):
    return render(request,'web/course.html')
def contact(request):
    return render(request,'web/contact.html')
def main(request):
    return render(request,'web/main.html')




def index(request):
    context = {
     'course':courses.objects.all(),
      'category':courseCategory.objects.all()
    }
    if request.method=="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmpass = request.POST.get("confirmpass")

        if password==confirmpass:
            coustomer = User.objects.create_user(username,email,password)

            coustomer.save()

            return redirect("login")



    return render(request,'web/index.html',context)

def login1(request):
    if request.method=="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            return redirect("index")

    return render (request,'web/account/login.html')

@login_required(login_url="login")
def cart(request):
     return render(request,'web/cart/cart.html')

def logout_view(request):
    logout(request)
    
    return render(request,'web/index.html')

def course(request):
    context = {
     'course':courses1.objects.all()
    }

    return render(request,'web/course.html',context)

def checkout(request):
    return render(request,'web/cart/checkout.html')


def contact(request):

    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Form=form(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        Form.save()
    return render(request,'web/contact.html')        


