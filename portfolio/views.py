from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from datetime import datetime
import sys

# Create your views here.


def home(request):
    success = False
    basics = basic.objects.all()
    educations = education.objects.all()
    experiances = experiance.objects.all()
    cat = category.objects.all()
    prod = product.objects.all()
    # email="shazaibrehman127@gmail.com"
    # is ke zriye ham dynamic search kr rhe he
    # abouts= about.objects.filter(Q(email__icontains=email))
    abouts= about.objects.all().order_by('-id')[:1]
    print(about)
    introduction = intro.objects.all()
    test = testimonial.objects.all()
    service = services.objects.all()
    if 'submit' in request.POST:
        data = request.POST
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        sub = 'Your Booking Has Been Registered'
        from_email = settings.EMAIL_HOST_USER
        data = {'name': name, 'email': email, }
        html = get_template('mail.html').render(data)
        msg = EmailMultiAlternatives(sub, '', from_email, [email])
        msg.attach_alternative(html, 'text/html')
        msg.send()
        contacts = contact.objects.create(
            name=name, email=email, subject=subject, message=message)
        if contact:
            success = True

    d = {'basic': basics, 'education': educations,
         'experiance': experiances, 'category': cat, 'product': prod, 'about': abouts, 'intro': introduction, 'testimonial': test, 'services': service, 'success': success}
    return render(request, 'index.html', d)

def admin_mini(request):
    if 'login' in request.POST:
        data=request.POST
        username=data['username']
        password=data['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        messages.error(request, 'Please Fill Correct Info.')
    return render(request,'admin.html')

def dashboard(request):
    return render(request,'dashboard.html')

def About_admin(request):
    sys.setrecursionlimit(1500)

    if 'abouts' in request.POST:
        detail=request.POST
        title=detail['title']
        email=detail['email']
        dob=detail['dob']
        age=detail['age']
        website=detail['website']
        mobile=detail['mobile']
        degree=detail['degree']
        city=detail['city']
        country=detail['country']
        availability=detail['available']
        img1=request.FILES['image']
        short=detail['short']
        abouts= about.objects.create(img=img1,head=title,email=email,dob=dob,age=age,website=website,mobile=mobile,degree=degree,city=city,country=country,freelance=availability,introduction=short)
        if about :
            messages.success(request,'details updated.')
            return render(request,'about-admin.html')
    return render(request,'about-admin.html')

def About_all(request):
    aboutus= about.objects.all()
    if 'delete' in request.POST:
        messages.success(request,'Record Deleted.')
        about.objects.filter(id=request.POST['delete']).delete()
        return redirect('about_all')

    d={'abouts':aboutus}
    return render(request,'about_all.html',d)

def about_update(request,about_id):
    abt=about.objects.get(id=about_id)
    
    if 'update' in request.POST:
        detail=request.POST

        title=detail['title']
        email=detail['email']
        dob=detail['dob']
        age=detail['age']
        website=detail['website']
        mobile=detail['mobile']
        degree=detail['degree']
        city=detail['city']
        country=detail['country']
        availability=detail['available']
        print(request.FILES['image'])
        img1=request.FILES['image']
        short=detail['short']
        data=about.objects.update(img=img1,head=title,email=email,age=age,dob=dob,website=website,mobile=mobile,degree=degree,city=city,country=country,freelance=availability,introduction=short)
        if data:
            return redirect('about_all')
        else:
            return redirect('about_update')

    d={'about':abt}
    return render(request,'about_update.html',d)



def Logout(request):
    logout(request)
    return redirect('admin_mini')
