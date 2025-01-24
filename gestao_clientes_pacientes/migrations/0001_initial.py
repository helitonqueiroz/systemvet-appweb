# Generated by Django 5.1.5 on 2025-01-23 15:51

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Paciente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("especie", models.CharField(max_length=50)),
                ("raca", models.CharField(blank=True, max_length=100, null=True)),
                ("idade", models.PositiveIntegerField(blank=True, null=True)),
                ("historico_saude", models.TextField(blank=True, null=True)),
                ("data_cadastro", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tutor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("endereco", models.TextField(blank=True, null=True)),
                ("telefone", models.CharField(blank=True, max_length=15, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "cpf",
                    models.CharField(
                        max_length=14,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="CPF deve estar no formato 000.000.000-00",
                                regex="^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$",
                            )
                        ],
                    ),
                ),
                ("data_cadastro", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="HistoricoMedico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo_evento", models.CharField(max_length=50)),
                ("descricao", models.TextField()),
                ("data_evento", models.DateField()),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="historico_medico",
                        to="gestao_clientes_pacientes.paciente",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="paciente",
            name="tutor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pacientes",
                to="gestao_clientes_pacientes.tutor",
            ),
        ),
        migrations.CreateModel(
            name="Vacina",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_vacina", models.CharField(max_length=100)),
                ("data_aplicacao", models.DateField()),
                ("proxima_dose", models.DateField(blank=True, null=True)),
                (
                    "paciente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vacinas",
                        to="gestao_clientes_pacientes.paciente",
                    ),
                ),
            ],
        ),
    ]