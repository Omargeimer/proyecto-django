from django.urls import path
from myapp import views
from inicio import views as InicioViews
from django.contrib import admin
from django.conf import settings
from registros import views as views_registros 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.saludo),
    path('about/', views.about, name="About"),
    path('inicio/', views_registros.registros, name="Principal"),
    path('registrar/',views_registros.contacto,name="Contacto"),    
    path('formulario/', InicioViews.formulario, name="Formulario"),
    path('ejemplo/', InicioViews.ejemplo, name="Ejemplo"),
    path('contacto/',views_registros.registrar,name="Registrar"),
    path('consultaContacto/',views_registros.comentarios,name="Comentarios"),
    path('formEditarContacto/<int:id>/', views_registros.consultarComentarioIndividal, name="ConsultaIndividual"),
    path('editarContacto/<int:id>/', views_registros.editarComentarioContacto, name="Editar"),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto,name='Eliminar'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)