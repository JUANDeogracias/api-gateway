from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers

class Usuario(models.Model):
    nombre = models.CharField(blank=False, max_length=150)
    primer_apellido = models.CharField(blank=True, null=True, max_length=250)

    # Función para validar si los campos están rellenos
    def clean(self):
        content = [self.nombre,self.primer_apellido]

        if any(not c for c in content) :
            raise ValidationError('Todos los campos deben de estar rellenos')
    def __str__(self):
        return f"{self.primer_apellido} "