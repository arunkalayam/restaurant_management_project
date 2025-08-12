from django.shortcuts import render

# Create your views here.
from django.shortcuts import settings

def homepage(request):
    context={
        'restaurant_name': settings.RESTUARANT_NAME
        'restuarant_phone':settings.RESTUARANT_PHONE
        }
        return render(request,'home.html',context)

def reservation(request):
    return render(request,'reservation.html')