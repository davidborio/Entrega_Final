"""proyecto_final URL Configuration

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
from django.urls import path
from HappyPaws.views import (index, aboutme, PetList,PetMineList,
                             PetDetail,PetCreate,PetUpdate,PetDelete,BuscarPet, SignUp, Login,Logout, 
                             ProfileCreate, ProfileUpdate, MensajeCreate, MensajeList, MensajeDelete, MensajeDetail,)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index, name="index"),
    path("",aboutme, name="aboutme"),    
    path("pet/list", PetList.as_view(), name="pet-list"),
    path("pet/list/mine", PetMineList.as_view(), name="pet-mine"),
    path("pet/<pk>/detail", PetDetail.as_view(), name="pet-detail"),
    path("pet/create", PetCreate.as_view(), name="pet-create"),
    path("pet/<pk>/update", PetUpdate.as_view(), name="pet-update"),
    path("pet/<pk>/delete", PetDelete.as_view(), name="pet-delete"),
    path("pet/buscar", BuscarPet.as_view(), name="pet-buscar"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/create", ProfileCreate.as_view(), name="profile-create"),
    path("profile/<pk>/update", ProfileUpdate.as_view(), name="profile-update"),
    path("mensaje/create", MensajeCreate.as_view(), name="mensaje-create"),
    path("mensaje/list", MensajeList.as_view(), name="mensaje-list"),
    path("mensaje/<pk>/delete", MensajeDelete.as_view(), name="mensaje-delete"),
    path("mensaje/<pk>/detail", MensajeDetail.as_view(), name="mensaje-detail"),
        
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)