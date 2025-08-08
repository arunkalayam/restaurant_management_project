from django.shortcuts import render

# Create your views here.
from django.shortcuts import settings

def homepage(request):
    context={
        'restaurant_name': settings.RESTUARANT_NAME
        }
        return render(request,'home.html',context)