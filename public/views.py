from django.shortcuts import render,redirect
from public.models import *

# Create your views here.


def abo(request):
    return render(request,'about.html')

def con(request):
    return render(request,'contact.html')

def ind(request):
    return render(request,'index.html')
def cou(request):
    return render(request,'courses.html')
def eve(request):
    return render(request,'events.html') 
def tra(request):
    return render(request,'trainers.html')
def reg(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        Gmail=request.POST.get('email')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        data=register.objects.create(firstname=fname,lastname=lname,Gmail=Gmail,password=password,Gender=gender,usertype='user')
        b="Registered succesfully ||"
        return render(request,'register.html',{'b':b})
    return render(request,'register.html') 

def login(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if register.objects.filter(Gmail=username,password=password):
            data=register.objects.get(Gmail=username,password=password)
            if data.usertype=="adm":
                request.session['admind']=data.id
                return redirect('/admind')
            elif data.usertype=="user":
                user=data.Gmail
                upass=data.password
                us=register.objects.get(Gmail=user,password=upass)
                request.session['userid']=us.id
                return redirect ('/userind')
            else:
                d="INVALID USERNAME OR PASSWORD"
                return render(request,'register.html',{'m':d})
    return render(request,'login.html')                
