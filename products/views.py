from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ProductsView(request):
    return render(request,'products_page.html',context={'title':"product's Page"})