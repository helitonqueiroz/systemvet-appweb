from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('tutores/', views.lista_tutores, name='lista_tutores'),
    path('tutores/<int:tutor_id>/', views.detalhes_tutor, name='detalhes_tutor'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/<int:paciente_id>/', views.detalhes_paciente, name='detalhes_paciente'),
    path('historico/', views.historico, name='historico'),
    path('configuracoes/', views.configuracoes, name='configuracoes'),
    path('search/', views.search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
