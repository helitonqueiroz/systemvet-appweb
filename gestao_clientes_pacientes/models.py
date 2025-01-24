from django.db import models
from django.core.validators import MinValueValidator, RegexValidator

class Tutor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Tutor")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    telefone = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Número de telefone inválido.')],
        verbose_name="Telefone"
    )
    email = models.EmailField(verbose_name="E-mail")
    cpf = models.CharField(
        max_length=11,
        validators=[RegexValidator(r'^\d{11}$', 'CPF deve conter 11 dígitos numéricos.')],
        verbose_name="CPF"
    )

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    ESPECIES_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('pássaro', 'Pássaro'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome do Paciente")
    especie = models.CharField(
        max_length=50,
        choices=ESPECIES_CHOICES,
        verbose_name="Espécie"
    )
    raca = models.CharField(max_length=100, verbose_name="Raça", blank=True, null=True)
    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento", blank=True, null=True
    )
    peso_kg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Peso (kg)",
        validators=[MinValueValidator(0.1, "Peso deve ser maior que zero.")],
    )
    historico_saude = models.TextField(verbose_name="Histórico de Saúde", blank=True)
    tutor = models.ForeignKey(
        Tutor, related_name='pacientes', on_delete=models.CASCADE, verbose_name="Tutor"
    )

    def __str__(self):
        return f"{self.nome} ({self.get_especie_display()})"

    @property
    def idade_aproximada(self):
        """Calcula a idade aproximada do paciente com base na data de nascimento."""
        from datetime import date

        if self.data_nascimento:
            hoje = date.today()
            anos = hoje.year - self.data_nascimento.year
            if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
                anos -= 1
            return anos
        return "Data de nascimento não informada."

class HistoricoMedico(models.Model):
    paciente = models.ForeignKey(
        Paciente, related_name="historico_medico", on_delete=models.CASCADE
    )
    tipo_evento = models.CharField(max_length=100, verbose_name="Tipo de Evento")
    data_evento = models.DateField(verbose_name="Data do Evento")
    descricao = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return f"{self.tipo_evento} - {self.data_evento}"

