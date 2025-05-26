from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.timezone import localdate

from .models import Laboratorio, Reserva
from .forms import LaboratorioForm, RegisterForm, ReservaForm

def home(request):
    atualizar_disponibilidade_laboratorios()
    return render(request, 'labs/home.html')



class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'labs/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso. Faça login para continuar.')
            return redirect('login')
        return render(request, 'labs/register.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('home')


class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = 'labs/laboratorios.html'
    context_object_name = 'laboratorios'

    def get_queryset(self):
        return Laboratorio.objects.filter(disponivel=True)


from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Laboratorio, Reserva

from django.utils.timezone import now

def laboratorio_detail(request, pk):
    laboratorio = get_object_or_404(Laboratorio, id=pk)
    hoje = localdate()

    # 🔁 Verifica reservas futuras ou em andamento
    reservas_ativas = Reserva.objects.filter(
        laboratorio=laboratorio,
        data=hoje,
        hora_fim__gte=now().time()
    )

    # ⛔ Se não houver reservas futuras ou em andamento, libera o laboratório
    if not reservas_ativas.exists():
        laboratorio.disponivel = True
        laboratorio.save()

    # Mostra as reservas de hoje
    reservas_hoje = Reserva.objects.filter(
        laboratorio=laboratorio,
        data=hoje
    ).order_by('hora_inicio')

    return render(request, 'labs/laboratorio_detail.html', {
        'laboratorio': laboratorio,
        'reservas_hoje': reservas_hoje,
    })





# ✅ View de reserva com aprovação automática
@login_required
def reservar_laboratorio(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.status = 'indisponivel'  # Ocupa o laboratório
            reserva.save()
            messages.success(request, 'Reserva feita com sucesso.')
            return redirect('minhas_reservas')
    else:
        form = ReservaForm()
    return render(request, 'labs/reservar.html', {'form': form})



@login_required
def minhas_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'labs/minhas_reservas.html', {'reservas': reservas})


@login_required
def cancelar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk, usuario=request.user)
    if reserva.status != 'cancelado':
        reserva.status = 'cancelado'
        reserva.save()
        messages.success(request, 'Reserva cancelada com sucesso.')
    return redirect('minhas_reservas')


@user_passes_test(lambda u: u.is_staff)
def admin_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'labs/admin/laboratorios.html', {'laboratorios': laboratorios})


@user_passes_test(lambda u: u.is_staff)
def admin_add_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'labs/admin/add_laboratorio.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def admin_edit_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('admin_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'labs/admin/edit_laboratorio.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def admin_delete_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    laboratorio.delete()
    return redirect('admin_laboratorios')


from django.utils import timezone
from datetime import datetime

def atualizar_disponibilidade_laboratorios():
    agora = timezone.localtime()

    laboratorios = Laboratorio.objects.all()
    for lab in laboratorios:
        reservas_ativas = Reserva.objects.filter(
            laboratorio=lab,
            data=agora.date(),
            hora_fim__gt=agora.time()
        )
        # Se não há reservas ativas, o laboratório está disponível
        lab.disponivel = not reservas_ativas.exists()
        lab.save()



from django.http import JsonResponse
from django.shortcuts import render
from .models import Reserva

def calendario(request):
    return render(request, 'labs/calendario.html')

def eventos_json(request):
    reservas = Reserva.objects.all()
    eventos = []

    for reserva in reservas:
        eventos.append({
            'title': f"{reserva.laboratorio.nome}",
            'start': f"{reserva.data}T{reserva.hora_inicio}",
            'end': f"{reserva.data}T{reserva.hora_fim}",
            'color': '#f59e0b' if reserva.status == 'indisponivel' else '#10b981'
        })

    return JsonResponse(eventos, safe=False)
