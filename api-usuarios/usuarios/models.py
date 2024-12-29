from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers

# 'id', 'username', 'email', 'first_name', 'last_name'
class Usuario(models.Model):
    username = models.CharField(blank=False, max_length=150)
    email = models.EmailField(blank=False, unique=True)
    first_name = models.CharField(blank=True, null=True, max_length=250)
    last_name = models.CharField(blank=True,null=True, max_length=250)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"