from django.shortcuts import render

def configuracoes(request):
    return render(request, 'gestao_clientes_pacientes/configuracoes.html')
