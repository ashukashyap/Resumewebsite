from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages


# Create your views here.

def Home(request):
    context = {'index':'active'}
    return render(request,'home/index.html',context)
    # return HttpResponse(" this is resume")


def Exprince(request):
    context = {'exprince':'active'}
    return render(request,'home/exprince.html',context) 


def Edu(request):
    context = {'edu':'active'}
    return render(request,'home/edu.html',context) 


def Skils(request):
    context = {'skils':'active'}
    return render(request,'home/skils.html',context)


def contact(request):
    
    if request.method == "POST":
        
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']


        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5 :
            messages.success(request,"Plese fill the form Correctly")
        else:
            contact = Contact(name = name, phone = phone, email=email,content=content ,timestamp = datetime.today()) 
            contact.save()
            messages.success(request,'Your message has been Sand ')
       


    context = {'contact':'active'}
    return render(request,'home/contact.html',context)
