from django.shortcuts import render, HttpResponse 
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is my first django app")

def about(request):
    return render(request, 'About.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')   
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, created=datetime.today())
        contact.save()
        messages.success(request, 'Your enquiry has been submitted successfully!!!')
    return render(request, 'Contact.html')

def variableProfile(request):
    context={
        "name":"Priya",
    }
    return render(request, 'DemoProfile.html', context)

def service_soft_dev(request):
    return render(request, 'services/software_development.html')

def service_ml(request):
    return render(request, 'services/machine_learning.html')

def service_cloud_serv(request):
    return render(request, 'services/cloud_services.html')