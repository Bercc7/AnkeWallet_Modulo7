from django import forms
from .models import Cuenta, Transaccion

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['nombre_cuenta']
        widgets = {
            'nombre_cuenta': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: 1px solid #cac4d0;', 'placeholder': 'Ej. Cuenta de Ahorros o Billetera'}),
        }

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['tipo', 'monto', 'descripcion', 'categorias']
        widgets = {
            'tipo': forms.Select(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: 1px solid #cac4d0;'}),
            'monto': forms.NumberInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: 1px solid #cac4d0;', 'placeholder': 'Ej. 5000'}),
            'descripcion': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: 1px solid #cac4d0;', 'placeholder': 'Detalle de la transacción...'}),
            'categorias': forms.SelectMultiple(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 8px; border: 1px solid #cac4d0;'}),
        }