from django.shortcuts import render,redirect
from adm.models import *
from adm.models import Files

# Create your views here.
def userind(request):
    return render(request,'userindex.html')

def userabo(request):
    return render(request,'userabo.html')    

def logout(request):
    request.session.flush()
    return redirect('/')

def uviewfile(request):
    d=Files.objects.all()
    return render(request,'uviewfile.html',{'d':d})

def ucontact(request):
    return render(request,'ucontact.html')                 
