# from django.core.management.base import BaseCommand
# from django.utils import timezone
# from labs.models import Reserva

# class Command(BaseCommand):
#     help = 'Atualiza status das reservas expiradas para disponível'

#     def handle(self, *args, **kwargs):
#         agora = timezone.localtime().time()
#         hoje = timezone.localdate()

#         reservas_expiradas = Reserva.objects.filter(
#             data=hoje,
#             hora_fim__lt=agora,
#             status='indisponivel'
#         )

#         for reserva in reservas_expiradas:
#             reserva.status = 'disponivel'
#             reserva.save()
#             self.stdout.write(f"✔ Reserva {reserva} atualizada para disponível.")

from django.core.management.base import BaseCommand
from labs.models import Laboratorio
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com 30 laboratórios fictícios'

    def handle(self, *args, **kwargs):
        Laboratorio.objects.all().delete()  # Limpa os dados existentes (opcional)

        recursos_exemplos = [
            "Projetor, Quadro branco, Ar condicionado",
            "Computadores, Impressora 3D",
            "Mesas ergonômicas, Kit de robótica",
            "Internet de alta velocidade, Estação meteorológica",
            "Smart TV, Microscópios",
        ]

        for i in range(1, 31):
            Laboratorio.objects.create(
                nome=f"Laboratório {i}",
                descricao=f"Espaço dedicado a atividades práticas e experimentais número {i}.",
                capacidade=random.randint(10, 40),
                recursos=random.choice(recursos_exemplos),
                disponivel=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('✅ 30 laboratórios foram criados com sucesso!'))

