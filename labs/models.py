# labs/models.py
from django.contrib.auth import get_user_model

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser  # Importação adicionada
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Laboratorio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    capacidade = models.PositiveIntegerField()
    recursos = models.TextField(blank=True, null=True)  # <-- Novo campo
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


from django.db import models
from django.contrib.auth import get_user_model
from .models import Laboratorio

from django.db import models
from django.contrib.auth import get_user_model

from datetime import datetime, time

class Reserva(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('indisponivel', 'Indisponível'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='indisponivel')

    @property
    def status_atual(self):
        agora = datetime.now()
        hoje = agora.date()
        agora_hora = agora.time()

        if self.data > hoje:
            return 'disponivel'
        elif self.data == hoje and self.hora_fim > agora_hora:
            return 'disponivel'
        return 'indisponivel'

