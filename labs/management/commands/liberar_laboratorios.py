from django.core.management.base import BaseCommand
from django.utils import timezone
from labs.models import Reserva

class Command(BaseCommand):
    help = 'Atualiza status das reservas expiradas para disponível'

    def handle(self, *args, **kwargs):
        agora = timezone.localtime().time()
        hoje = timezone.localdate()

        reservas_expiradas = Reserva.objects.filter(
            data=hoje,
            hora_fim__lt=agora,
            status='indisponivel'
        )

        for reserva in reservas_expiradas:
            reserva.status = 'disponivel'
            reserva.save()
            self.stdout.write(f"✔ Reserva {reserva} atualizada para disponível.")
