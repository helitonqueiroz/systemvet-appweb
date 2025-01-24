from django.contrib import admin
from django.urls import path, include  # Adicionar o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestao_clientes_pacientes.urls')),  # Incluir as URLs do app
]
