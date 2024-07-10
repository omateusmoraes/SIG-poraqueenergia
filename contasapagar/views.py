from django.shortcuts import render, redirect, get_object_or_404
from .models import Contasapagar  # Corrigido o nome do modelo importado
from .forms import ContasapagarForm

def contasapagar_list(request):
    contasapagar = Contasapagar.objects.all()
    form = ContasapagarForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('contasapagar_list')
    return render(request, contasapagar_form.html, {'contasapagar': contasapagar})

def add_contasapagar(request):
    if request.method == 'POST':
        form = ContasapagarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contasapagar_list')
    else:
        form = ContasapagarForm()
    return render(request, 'contasapagar_form.html', {'form': form})

def edit_contasapagar(request, pk):
    contasapagar = get_object_or_404(Contasapagar, pk=pk)  # Corrigido o nome do modelo
    if request.method == 'POST':
        form = ContasapagarForm(request.POST, instance=contasapagar)
        if form.is_valid():
            form.save()
            return redirect('contasapagar_list')
    else:
        form = ContasapagarForm(instance=contasapagar)
    return render(request, 'contasapagar_form.html', {'form': form})

def delete_contasapagar(request, pk):
    contasapagar = get_object_or_404(Contasapagar, pk=pk)
    if request.method == 'POST':
        contasapagar.delete()
        return redirect('contasapagar_list')
    else:
        form = ContasapagarForm(instance=contasapagar)
    return render(request, 'contasapagar_confirm_delete.html', {'contasapagar': contasapagar, 'form': form})
