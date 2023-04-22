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
from HappyPaws.views import (index, FormPrueba, crearmascota, PetList,
                             PetDetail,PetCreate,PetUpdate,PetDelete,BuscarPet, SignUp, Login,Logout)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index, name="index"),
    path("formulario", FormPrueba),
    path("crear_mascota", crearmascota, name="crear-mascota"),
    path("pet/list", PetList.as_view(), name="pet-list"),
    path("pet/<pk>/detail", PetDetail.as_view(), name="pet-detail"),
    path("pet/create", PetCreate.as_view(), name="pet-create"),
    path("pet/<pk>/update", PetUpdate.as_view(), name="pet-update"),
    path("pet/<pk>/delete", PetDelete.as_view(), name="pet-delete"),
    path("pet/buscar", BuscarPet.as_view(), name="pet-buscar"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout")
    
    ]