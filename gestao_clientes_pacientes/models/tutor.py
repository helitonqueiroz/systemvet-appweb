from django.db import models
from django.core.validators import RegexValidator

class Tutor(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField(null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    cpf = models.CharField(
        max_length=14,
        unique=True,
        validators=[RegexValidator(regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', message='CPF deve estar no formato 000.000.000-00')]
    )
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
