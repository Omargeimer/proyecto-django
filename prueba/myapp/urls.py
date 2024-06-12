from django.urls import path
from myapp import views
from inicio import views as InicioViews

urlpatterns = [
    path('', views.saludo),
    path('about/', views.about, name="About"),
    path('inicio/', InicioViews.principal, name="Principal"),
    path('contacto/', InicioViews.contacto, name="Contacto"),
    path('formulario/', InicioViews.formulario, name="Formulario"),
    path('ejemplo/', InicioViews.ejemplo, name="Ejemplo"),
]