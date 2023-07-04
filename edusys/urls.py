"""edusys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from public.views import *
from user.views import *
from adm.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_file/',upload_file, name='upload_file'),
    path('abo',abo),
    path('con',con),
    path('',ind),
    path('cou',cou),
    path('login',login),
    path('cou',cou),
    path('eve',eve),
    path('tra',tra),
    path('reg',reg),
    path('logout',logout),
    path('userind',userind),
    path('userabo',userabo),
    path('admind',admind),
    path('viewuser',viewuser),
    path('viewfile',viewfile),
    path('uviewfile',uviewfile),
    path('ucontact',ucontact),
    # path('deletefile/<int:id>',deletefile),
   

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
