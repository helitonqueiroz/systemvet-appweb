from django.shortcuts import render, get_object_or_404
from ..models import Paciente

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'gestao_clientes_pacientes/lista_pacientes.html', {'pacientes': pacientes})

def detalhes_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    return render(request, 'gestao_clientes_pacientes/detalhes_paciente.html', {'paciente': paciente})

def historico(request):
    pacientes = Paciente.objects.all()
    return render(request, 'gestao_clientes_pacientes/historico.html', {'pacientes': pacientes})

def search(request):
    query = request.GET.get('query')
    filter_cliente = request.GET.get('filter-cliente')
    filter_paciente = request.GET.get('filter-paciente')
    filter_especie = request.GET.get('filter-especie')
    filter_cpf = request.GET.get('filter-cpf')
    
    # Lógica de busca e filtragem aqui
    results = []  # Substitua com a lógica de busca real
    
    return render(request, 'gestao_clientes_pacientes/search_results.html', {'results': results})
