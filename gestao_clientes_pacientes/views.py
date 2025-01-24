from django.shortcuts import render, get_object_or_404
from .models import Tutor, Paciente

def home(request):
    return render(request, 'gestao_clientes_pacientes/home.html')

def lista_tutores(request):
    tutores = Tutor.objects.all()
    return render(request, 'gestao_clientes_pacientes/lista_tutores.html', {'tutores': tutores})

def detalhes_tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    return render(request, 'gestao_clientes_pacientes/detalhes_tutor.html', {'tutor': tutor})

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'gestao_clientes_pacientes/lista_pacientes.html', {'pacientes': pacientes})

def detalhes_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    return render(request, 'gestao_clientes_pacientes/detalhes_paciente.html', {'paciente': paciente})

def historico(request):
    pacientes = Paciente.objects.all()
    return render(request, 'gestao_clientes_pacientes/historico.html', {'pacientes': pacientes})

def configuracoes(request):
    return render(request, 'gestao_clientes_pacientes/configuracoes.html')

def search(request):
    query = request.GET.get('query')
    filter_cliente = request.GET.get('filter-cliente')
    filter_paciente = request.GET.get('filter-paciente')
    filter_especie = request.GET.get('filter-especie')
    filter_cpf = request.GET.get('filter-cpf')
    
    # Lógica de busca e filtragem aqui
    results = []  # Substitua com a lógica de busca real
    
    return render(request, 'gestao_clientes_pacientes/search_results.html', {'results': results})

