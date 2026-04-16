from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion, Categoria

admin.site.register(Cliente)
admin.site.register(Cuenta)
admin.site.register(Transaccion)
admin.site.register(Categoria)