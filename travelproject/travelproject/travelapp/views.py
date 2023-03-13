from django.http import HttpResponse
from django.shortcuts import render

from . models import place


def about(request):
      x= place.objects.all()
      # return render(request,"index.html")
      return render(request,"index.html",{'result':x})

