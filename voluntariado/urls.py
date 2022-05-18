from django.urls import path
from . import views


urlpatterns = [
    path("nuevo_voluntario/", views.nuevo_voluntario, name="NuevoVoluntario"),
    path("facilitadores/", views.facilitadores, name="Facilitadores"),
    path("nuevo_facilitador/", views.nuevo_facilitador, name="NuevoFacilitador"),
    path("facilitador/<id>", views.ver_facilitador, name="VerFacilitador"),
    path('buscar/<nombre>/', views.buscar_voluntario, name="BuscarVoluntario"),
    path('buscar/resultados', views.resultados_vol, name="BuscarResultados"),
]
