from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Reserva, Laboratorio  # ✅ Seus modelos vêm daqui

from django import forms
from django.contrib.auth import get_user_model
from .models import Reserva, Laboratorio
from django.core.exceptions import ValidationError
import datetime

from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['laboratorio', 'data', 'hora_inicio', 'hora_fim']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].widget = forms.DateInput(
            attrs={
                'class': 'form-control datepicker',
                'placeholder': 'DD/MM/AAAA',
                'autocomplete': 'off',
                'id': 'data-reserva'  # Adicionamos um ID para facilitar a seleção
            }
        )
    

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



# forms.py
class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nome', 'descricao', 'capacidade', 'recursos', 'disponivel']


