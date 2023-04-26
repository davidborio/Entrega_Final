from django import forms

class PetForms(forms.Form):
    nombre = forms.CharField(max_length= 50)
    raza = forms.CharField(max_length= 50)
    fecha = forms.DateField()
    tel= forms.CharField(max_length=30)
    mail=forms.EmailField(max_length=50)
    estado=forms.CharField(max_length=100)
    ciudad=forms.CharField(max_length=50)
    descripcion=forms.CharField(max_length=300)

class BuscarPetForm(forms.Form):
    criterio_raza=forms.CharField(max_length= 50)
    criterio_ciudad=forms.CharField(max_length=50)
