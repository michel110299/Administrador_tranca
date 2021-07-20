from django.contrib import admin
from django.urls import path
from adm.views import ViewCadastro,ViewInicioJogo,ViewResultado,ViewInfo,ViewInicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ViewInicio,name="Inicio"),
    path('cadastro-jogo',ViewCadastro,name="cadastro"),
    path('inicio-jogo/<int:idJogo>/',ViewInicioJogo,name="InicioJogo"),
    path('resultado-jogo/<int:idJogo>/',ViewResultado,name="Resultado"),
    path('info-rodada/<int:idPartida>/',ViewInfo,name="Info_rodada"),
]
