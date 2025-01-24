from django.db import models
from .paciente import Paciente

class Vacina(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='vacinas')
    nome_vacina = models.CharField(max_length=100)
    data_aplicacao = models.DateField()
    proxima_dose = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome_vacina
