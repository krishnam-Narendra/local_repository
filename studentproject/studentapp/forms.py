from django import forms
from .models import StudentRegister

class StudentRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = StudentRegister
        fields = '__all__'

