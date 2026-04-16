from django.test import TestCase
from django.contrib.auth.models import User
from .models import Proyecto, Tarea

class ProyectoModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='tester', password='password123')
        
        self.proyecto = Proyecto.objects.create(
            nombre='Proyecto de Testing',
            descripcion='Probando que el sistema funcione.',
            usuario=self.usuario
        )

    def test_creacion_proyecto(self):

        self.assertEqual(self.proyecto.nombre, 'Proyecto de Testing')
        
        self.assertEqual(self.proyecto.usuario.username, 'tester')
        
        self.assertEqual(str(self.proyecto), 'Proyecto de Testing')