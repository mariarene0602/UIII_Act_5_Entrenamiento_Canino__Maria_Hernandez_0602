from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .models import Perro
from .models import Entrenamiento

def inicio_entrenamiento_canino(request):
    return render(request, 'inicio.html')

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']
        fecha_registro = request.POST['fecha_registro']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        comentarios = request.POST.get('comentarios', '')
        
        cliente = Cliente(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            fecha_registro=fecha_registro,
            fecha_nacimiento=fecha_nacimiento,
            comentarios=comentarios
        )
        cliente.save()
        return redirect('ver_cliente')
    
    return render(request, 'clientes/agregar_cliente.html')

def ver_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/ver_cliente.html', {'clientes': clientes})

def actualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    return render(request, 'clientes/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, id_cliente):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
        cliente.nombre = request.POST['nombre']
        cliente.direccion = request.POST['direccion']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST['email']
        cliente.fecha_registro = request.POST['fecha_registro']
        cliente.fecha_nacimiento = request.POST['fecha_nacimiento']
        cliente.comentarios = request.POST.get('comentarios', '')
        cliente.save()
        return redirect('ver_cliente')
    
    return redirect('ver_cliente')

def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    
    return render(request, 'clientes/borrar_cliente.html', {'cliente': cliente})


# ==========================================
# VISTAS PARA PERROS
# ==========================================

def agregar_perro(request):
    clientes = Cliente.objects.all()
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        nombre = request.POST['nombre']
        raza = request.POST['raza']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        color = request.POST['color']
        peso = request.POST['peso']
        
        cliente = Cliente.objects.get(id_cliente=cliente_id)
        perro = Perro(
            cliente=cliente,
            nombre=nombre,
            raza=raza,
            fecha_nacimiento=fecha_nacimiento,
            color=color,
            peso=peso
        )
        perro.save()
        return redirect('ver_perro')
    
    return render(request, 'perros/agregar_perro.html', {'clientes': clientes})

def ver_perro(request):
    perros = Perro.objects.all()
    return render(request, 'perros/ver_perro.html', {'perros': perros})

def actualizar_perro(request, id_perro):
    perro = get_object_or_404(Perro, id_perro=id_perro)
    clientes = Cliente.objects.all()
    return render(request, 'perros/actualizar_perro.html', {'perro': perro, 'clientes': clientes})

def realizar_actualizacion_perro(request, id_perro):
    if request.method == 'POST':
        perro = get_object_or_404(Perro, id_perro=id_perro)
        cliente_id = request.POST['cliente']
        perro.cliente = Cliente.objects.get(id_cliente=cliente_id)
        perro.nombre = request.POST['nombre']
        perro.raza = request.POST['raza']
        perro.fecha_nacimiento = request.POST['fecha_nacimiento']
        perro.color = request.POST['color']
        perro.peso = request.POST['peso']
        perro.save()
        return redirect('ver_perro')
    
    return redirect('ver_perro')

def borrar_perro(request, id_perro):
    perro = get_object_or_404(Perro, id_perro=id_perro)
    if request.method == 'POST':
        perro.delete()
        return redirect('ver_perro')
    
    return render(request, 'perros/borrar_perro.html', {'perro': perro})

# ==========================================
# VISTAS PARA ENTRENAMIENTOS
# ==========================================

def agregar_entrenamiento(request):
    perros = Perro.objects.all()
    if request.method == 'POST':
        perro_id = request.POST['perro']
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        fecha_inicio = request.POST['fecha_inicio']
        duracion_horas = request.POST['duracion_horas']
        lugar = request.POST['lugar']
        nivel = request.POST['nivel']
        costo = request.POST['costo']
        
        perro = Perro.objects.get(id_perro=perro_id)
        entrenamiento = Entrenamiento(
            perro=perro,
            nombre=nombre,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            duracion_horas=duracion_horas,
            lugar=lugar,
            nivel=nivel,
            costo=costo
        )
        entrenamiento.save()
        return redirect('ver_entrenamiento')
    
    return render(request, 'entrenamientos/agregar_entrenamiento.html', {'perros': perros})

def ver_entrenamiento(request):
    entrenamientos = Entrenamiento.objects.all()
    return render(request, 'entrenamientos/ver_entrenamiento.html', {'entrenamientos': entrenamientos})

def actualizar_entrenamiento(request, id_entrenamiento):
    entrenamiento = get_object_or_404(Entrenamiento, id_entrenamiento=id_entrenamiento)
    perros = Perro.objects.all()
    return render(request, 'entrenamientos/actualizar_entrenamiento.html', {'entrenamiento': entrenamiento, 'perros': perros})

def realizar_actualizacion_entrenamiento(request, id_entrenamiento):
    if request.method == 'POST':
        entrenamiento = get_object_or_404(Entrenamiento, id_entrenamiento=id_entrenamiento)
        perro_id = request.POST['perro']
        entrenamiento.perro = Perro.objects.get(id_perro=perro_id)
        entrenamiento.nombre = request.POST['nombre']
        entrenamiento.descripcion = request.POST['descripcion']
        entrenamiento.fecha_inicio = request.POST['fecha_inicio']
        entrenamiento.duracion_horas = request.POST['duracion_horas']
        entrenamiento.lugar = request.POST['lugar']
        entrenamiento.nivel = request.POST['nivel']
        entrenamiento.costo = request.POST['costo']
        entrenamiento.save()
        return redirect('ver_entrenamiento')
    
    return redirect('ver_entrenamiento')

def borrar_entrenamiento(request, id_entrenamiento):
    entrenamiento = get_object_or_404(Entrenamiento, id_entrenamiento=id_entrenamiento)
    if request.method == 'POST':
        entrenamiento.delete()
        return redirect('ver_entrenamiento')
    
    return render(request, 'entrenamientos/borrar_entrenamiento.html', {'entrenamiento': entrenamiento})