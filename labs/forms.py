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
        widgets = {
            'data': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'hora_inicio': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'hora_fim': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'laboratorio': forms.Select(attrs={'class': 'form-control'})
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



# forms.py
class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nome', 'descricao', 'capacidade', 'recursos', 'disponivel']


