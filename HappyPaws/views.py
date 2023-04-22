from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DetailView,DeleteView
#from django.views.generic.detail import DetailView
from HappyPaws.models import Pet
from HappyPaws.forms import PetForms,BuscarPetForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

def index(request):
    return render(request,"HappyPaws/index.html")

def FormPrueba(request):
    return render(request, "HappyPaws/FormPrueba.html")


def crearmascota(request):
    f=PetForms()
    f=PetForms(request.POST)
    context = {'f':f}


    return render(request,"HappyPaws/crear_mascota.html",context)

class PetList(ListView):
    model=Pet

class PetDetail(DetailView):
    model=Pet

class PetCreate(LoginRequiredMixin,CreateView):
    model=Pet
    success_url= reverse_lazy("pet-list")
    fields="__all__"

class PetUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Pet
    success_url= reverse_lazy("pet-list")
    fields="__all__"

    def test_func(self):
        user_id = self.request.user.id
        pet_id = self.kwargs.get("pk")
        return Pet.objects.filter(owner=user_id, id=pet_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"HappyPaws/not_found.html")

class PetDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Pet
    success_url= reverse_lazy("pet-list")

    def test_func(self):
        user_id = self.request.user.id
        pet_id = self.kwargs.get("pk")
        return Pet.objects.filter(owner=user_id, id=pet_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"HappyPaws/not_found.html")

class BuscarPet(ListView):
    model=Pet
    
    def get_queryset(self):
        f = BuscarPetForm(self.request.GET)
        if f.is_valid():
                return Pet.objects.filter(raza__icontains= f.data["criterio_raza"]).all() #__icontains filtra todas las palabras que contengan la cadena ingresada en nombre

        return Pet.objects.none()
    
class SignUp(CreateView):
    form_class=UserCreationForm
    template_name='registration/signup.html'
    success_url= reverse_lazy('index')

class Login(LoginView):
    next_page = reverse_lazy('index')

class Logout(LogoutView):
    template_name='registration/logout.html'



#PetList(List)

# Create your views here.