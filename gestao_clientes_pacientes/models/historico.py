from django.db import models
from .paciente import Paciente

class HistoricoMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='historico_medico')
    tipo_evento = models.CharField(max_length=50)  # Ex: Consulta, Tratamento
    descricao = models.TextField()
    data_evento = models.DateField()

    def __str__(self):
        return f"{self.tipo_evento} - {self.paciente.nome}"
