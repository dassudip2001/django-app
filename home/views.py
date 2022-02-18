from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about")


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("this is about")


def services(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,datetime=datetime.today())
        contact.save()

    return render(request, 'services.html')
    # return HttpResponse("this is services")
