from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm

def agendamento_list(request):
    appointments = Agendamento.objects.all()
    return render(request, 'agendamentos.html', {'appointments': appointments})

def add_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamento_list')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento_form.html', {'form': form})

def edit_agendamento(request, agendamento_id):
    appointment = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('agendamento_list')
    else:
        form = AgendamentoForm(instance=appointment)
    return render(request, 'agendamento_form.html', {'form': form})

def delete_agendamento(request, agendamento_id):
    appointment = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('agendamento_list')
    return render(request, 'agendamento_confirm_delete.html', {'appointment': appointment})



