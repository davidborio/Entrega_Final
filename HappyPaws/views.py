from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DetailView,DeleteView
#from django.views.generic.detail import DetailView
from HappyPaws.models import Pet,Profile,Mensaje
from HappyPaws.forms import PetForms,BuscarPetForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

def aboutme(request):
    return render(request,"HappyPaws/aboutme.html")

def index(request):
    context={
        "pets":Pet.objects.all()
    }
    return render(request,"HappyPaws/index.html",context)

class PetList(ListView):
    model=Pet 
    context_object_name= "pets"   

class PetMineList(LoginRequiredMixin, PetList):
    
    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user.id).all()


class PetDetail(DetailView):
    model=Pet

class PetCreate(LoginRequiredMixin,CreateView):
    model=Pet
    success_url= reverse_lazy("pet-list")
    fields="__all__"

class PetUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Pet
    success_url= reverse_lazy("pet-list")
    fields= ["nombre","raza","tel","mail","ciudad","estado","imagen","descripcion"]

    def test_func(self):
        user_id = self.request.user.id
        pet_id = self.kwargs.get("pk") # Obtiene el id del post a través de la url pasada
        return Pet.objects.filter(owner=user_id, id=pet_id).exists() # Verifica si existe el un post de ese usuario con ese id en la BD
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
                if f.data["criterio_ciudad"] == "":
                    return Pet.objects.filter(raza__icontains= f.data["criterio_raza"]).all() #__icontains filtra todas las palabras que contengan la cadena ingresada en nombre
                elif f.data["criterio_raza"] == "":
                    return Pet.objects.filter(ciudad__icontains= f.data["criterio_ciudad"]).all()
                 
        return Pet.objects.none()    

    
class SignUp(CreateView):
    form_class=UserCreationForm
    template_name='registration/signup.html'
    success_url= reverse_lazy('index')

class Login(LoginView):
    next_page = reverse_lazy('index')

class Logout(LogoutView):
    template_name='registration/logout.html'


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = ['avatar']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = ['avatar']

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()

class MensajeCreate(CreateView):
    model=Mensaje
    success_url= reverse_lazy("index")
    fields='__all__'

class MensajeList(LoginRequiredMixin, ListView):
    model=Mensaje
    context_object_name = "mensajes"
    success_url= reverse_lazy("index")
    fields='__all__'
    
    def get_queryset(self):
        return Mensaje.objects.filter(destinatario = self.request.user.id).all()

class MensajeDelete(DeleteView):
    model=Mensaje
    success_url= reverse_lazy("mensaje-list")

class MensajeDetail(DetailView):
    model=Mensaje





#PetList(List)

# Create your views here.