from rest_framework import serializers
from django.contrib.auth.models import User

from usuarios.Models.UsuarioModel import Usuario
from usuarios.Models.HorasModel import Horas

# DTO de usuarios
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','nombre','primer_apellido']

# DTO de horas
class HorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horas
        fields = "__all__"