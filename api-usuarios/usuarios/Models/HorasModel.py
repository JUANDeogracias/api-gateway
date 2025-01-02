from django.db import models
from usuarios.Models.UsuarioModel import Usuario


class Horas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='horas')
    fecha = models.DateField()
    horas = models.DecimalField(max_digits=5, decimal_places=2)  # Por ejemplo: 4.5 horas

    def __str__(self):
        return f"{self.fecha}: {self.horas} horas"