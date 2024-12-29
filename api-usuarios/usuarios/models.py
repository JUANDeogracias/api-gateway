from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers

class Usuario(models.Model):
    nombre = models.CharField(blank=False, max_length=150)
    email = models.EmailField(blank=False, unique=True)
    primer_apellido = models.CharField(blank=True, null=True, max_length=250)
    segundo_apellido = models.CharField(blank=True,null=True, max_length=250)

    def __str__(self):
        return f"{self.primer_apellido} {self.segundo_apellido}"