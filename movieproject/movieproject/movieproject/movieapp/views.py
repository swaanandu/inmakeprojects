from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.form import  movieform
from movieapp.models import Movie


def index(request):
    x=Movie.objects.all()
    return render(request,"index.html",{'res':x})
def detail(request,m_id):
    x=Movie.objects.get(id=m_id)
    return render(request,"detail.html",{'m':x})
def add(request):
    if request.method == 'POST':
        j = request.POST.get('name')
        k = request.POST.get('desc')
        l = request.POST.get('year')
        m = request.FILES['img']
        p=Movie(name=j,desc=k,year=l,img=m)
        p.save();
        return redirect('/')
    return render(request,"add.html")
def update(request,up_id):
     a=Movie.objects.get(id=up_id)
     b= movieform(request.POST or None,request.FILES,instance=a)
     if b.is_valid():
             b.save();
             return redirect('/')


     return render(request,"update.html",{'obj1':b,'obj2':a})


def delete(request,del_id):
    if request.method=='POST':
        t=Movie.objects.get(id=del_id)
        t.delete()
        return redirect('/')
    return render(request,"delete.html")