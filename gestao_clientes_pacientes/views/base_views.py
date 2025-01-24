from django.shortcuts import render

def home(request):
    return render(request, 'gestao_clientes_pacientes/home.html')
