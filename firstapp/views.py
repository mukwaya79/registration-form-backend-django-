from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def registerhere(request):

   firstname1 = request.POST.get("name")
   lastname1 = request.POST.get("ln")
   password1 = request.POST.get("password")
   email2 = request.POST.get("email")
   mobile1 = request.POST.get("num")
   address1 = request.POST.get("address")
   gender1 = request.POST.get("g")
   country1= request.POST.get("country")
   hobbies1 = request.POST.getlist("x[]")
   date1 = request.POST.get("datetoday")
   file2 = request.FILES.get("file")

   obj33 = Register(Firstname =firstname1, Lastname = lastname1, Password = password1, Email = email2, 
                       Mobile= mobile1, Address = address1, Gender = gender1, Country = country1,
                       Hobbies = hobbies1, Date = date1, File =file2)

   obj33.save()

   return render(request, 'firstapp/index.html',{"message": "Thank you for Registering with us"})

def next(request):

    return render(request, 'firstapp/index.html')