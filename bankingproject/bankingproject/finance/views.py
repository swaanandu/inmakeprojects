from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.
def register(request):

    if request.method== 'POST':
      x = request.POST['username']
      m = request.POST['password']
      n = request.POST['cpassword']
      if m==n:
        if User.objects.filter(username=x).exists():
            messages.info(request,"USER EXISTS")
        else:
              user=User.objects.create_user(username=x,password=m)
              user.save();
              messages.info(request,"Registration Success")
              return redirect('finance:login')
      else:
          messages.info(request,"Password not matching")
          return redirect('finance:register')

    return render(request,"register.html")
def login(request):
    if request.method=='POST':
        x=request.POST['username']
        y = request.POST['password']
        z=auth.authenticate(username=x,password=y)
        if z is not None:
            auth.login(request,z)
            messages.info(request,"Login Successfull")
            return redirect('finance:move')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('finance:login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def new(request):

    # return render(request,"index.html")
    return render(request, "new.html")

def success(request):

    # return render(request,"index.html")
    return render(request, "success.html")
def move(request):

    # return render(request,"index.html")
    return render(request, "move.html")
