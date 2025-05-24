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

class Reserva(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
        ('cancelado', 'Cancelado'),
    ]
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f'{self.laboratorio.nome} - {self.data} ({self.hora_inicio} - {self.hora_fim})'

