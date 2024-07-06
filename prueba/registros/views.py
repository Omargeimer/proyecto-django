from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): 
            form.save()
            return render(request, 'registros/consultaContacto.html')
    form = ComentarioContactoForm()

    return render(request, 'registros/contacto.html', {'form': form})


# Create your views here.
def eliminarComentarioContacto (request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultaContacto.html", {'coments':comentarios})
    
    return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividal (request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request,"registros/editarComentario.html",{'coment':comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultarContacto.html", {'coments':comentarios})
    return render(request,"registros/editarContacto.html", {'coment':comentario})


def comentarios(request):
    comentarios=ComentarioContacto.objects.all()
    return render(request, "registros/consultaContacto.html", {'coments':comentarios})

# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request, "registros/principal.html", {'9B':alumnos})

def contacto(request):
    return render(request,"registros/contacto.html")
    #Indicamos el lugar donde se renderizará el resultado de esta vista