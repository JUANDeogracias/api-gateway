from rest_framework import serializers
from django.contrib.auth.models import User

from usuarios.models import Usuario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'primer_apellido', 'segundo_apellido']
