from django.shortcuts import render, get_object_or_404
from ..models import Tutor

def lista_tutores(request):
    tutores = Tutor.objects.all()
    return render(request, 'gestao_clientes_pacientes/lista_tutores.html', {'tutores': tutores})

def detalhes_tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    return render(request, 'gestao_clientes_pacientes/detalhes_tutor.html', {'tutor': tutor})
