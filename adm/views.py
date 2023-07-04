from django.shortcuts import render,redirect
from adm.models import Files
from adm.models import *
from public.models import *
from user.models import *

# Create your views here.

def admind(request):
    return render(request,'admind.html')

def viewuser(request):
    d=register.objects.all().filter(usertype='user')
    return render(request,'viewuser.html',{'d':d})

def upload_file(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        files =  request.FILES['files']
        file_obj = Files(uname=uname, files=files)
        file_obj.save()
        return render(request,'admind.html')
    else:
        return render(request,'upload_file.html') 

def viewfile(request):
    d=Files.objects.all()
    return render(request,'viewfile.html',{'d':d})  

# def deletefile(request,id):
#     d=Files.objects.get(id=id)
#     d.delete()
#     return redirect('/viewfile')              
