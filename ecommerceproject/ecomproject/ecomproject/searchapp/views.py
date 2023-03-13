from django.db.models import Q
from django.shortcuts import render

from shop.models import Product


# Create your views here.
def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request,'search.html',{'query':query,'products':products})






# from django.shortcuts import render
# from django.db.models import Q

# def SearchResult(request):
#     if request.method == 'GET':
#         query= request.GET.get('q')
#
#         submitbutton= request.GET.get('submit')
#
#         if query is not None:
#             lookups= Q(name__contains=query) | Q(description__contains=query)
#
#             results= Product.objects.filter(lookups).distinct()
#
#
#             return render(request, 'search.html', {'query': submitbutton, 'products': results})
