from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cuenta, Transaccion, Cliente
from .forms import CuentaForm, TransaccionForm

@login_required
def home(request):
    cliente, created = Cliente.objects.get_or_create(usuario=request.user)
    cuentas = Cuenta.objects.filter(cliente=cliente)
    total_general = cuentas.aggregate(Sum('saldo'))['saldo__sum'] or 0.00

    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            nueva_cuenta = form.save(commit=False)
            nueva_cuenta.cliente = cliente
            nueva_cuenta.save()
            return redirect('home')
    else:
        form = CuentaForm()

    return render(request, 'home.html', {
        'cuentas': cuentas, 
        'form': form,
        'total_general': total_general
    })

@login_required
def detalle_cuenta(request, cuenta_id):
    cliente = Cliente.objects.get(usuario=request.user)
    cuenta = get_object_or_404(Cuenta, id=cuenta_id, cliente=cliente)
    transacciones = Transaccion.objects.filter(cuenta=cuenta).order_by('-fecha')

    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            transaccion = form.save(commit=False)
            transaccion.cuenta = cuenta
            
            if transaccion.tipo == 'ingreso':
                cuenta.saldo += transaccion.monto
            else:
                cuenta.saldo -= transaccion.monto
            
            cuenta.save()
            transaccion.save()
            form.save_m2m() 
            
            return redirect('detalle_cuenta', cuenta_id=cuenta.id)
    else:
        form = TransaccionForm()

    return render(request, 'detalle_cuenta.html', {
        'cuenta': cuenta, 
        'transacciones': transacciones, 
        'form': form
    })