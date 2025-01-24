from django.db import models
from .tutor import Tutor

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=100, null=True, blank=True)
    idade = models.PositiveIntegerField(null=True, blank=True)
    historico_saude = models.TextField(null=True, blank=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='pacientes')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
