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

def menu_list(request):
    try:
        menu_items=["Pizza","Paste","Garlic Chutney"]
    except DatabaseError:
        menu_items=[]
        error_message="Sorry we couldn't load menu"
        return render(request,'menu.html')

def restuarant_info(request):
    return{
        "RESTUARANT_HOURS":getattr(settings,"RESTUARANT_HOURS", "Mon-Fri: 11am-9pm Sat-Sun:10 am-4pm")
        
    }
def menu_list(request):
    menu=[
        {
            "name": "Pizza",
            "description": "Very Cheap",
        },
        {
            "name": "Rice",
            "description": "Very Good",

        }
    ]
      return response(menu)