from datetime import date

from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from usuarios.Models.HorasModel import Horas
from usuarios.serializers import HorasSerializer
from usuarios.Models.UsuarioModel import Usuario


class HorasViewSet(viewsets.ModelViewSet):
    queryset = Horas.objects.all()
    serializer_class = HorasSerializer

    @action(detail=False, methods=['post'])
    def add_horas(self, request):
        cantidad = request.data.get('cantidad', None)
        usuario_id = request.data.get('usuario_id', None)

        # Validar que los campos requeridos estén presentes
        if not cantidad or not usuario_id:
            return Response(
                {'error': 'Los campos "cantidad" y "usuario_id" son obligatorios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Validar que el usuario existe
            usuario = Usuario.objects.get(id=usuario_id)

            # Crear el registro de horas
            Horas.objects.create(
                usuario=usuario,
                fecha=date.today(),
                horas=float(cantidad)
            )
            return Response(
                {'success': 'Horas añadidas correctamente.'},
                status=status.HTTP_201_CREATED
            )
        except Usuario.DoesNotExist:
            return Response(
                {'error': 'Usuario no encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': f'Error al añadir horas: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['get'])
    def horas_por_mes(self, request):
        usuario_id = request.query_params.get('usuario_id', None)

        if not usuario_id:
            return Response(
                {'error': 'El parámetro "usuario_id" es obligatorio.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            usuario = Usuario.objects.get(id=usuario_id)
            print(f"Usuario encontrado: {usuario}")

            horas_por_mes = (
                Horas.objects.filter(usuario=usuario)
                .values('fecha__year', 'fecha__month')
                .annotate(total_horas=Sum('horas'))
                .order_by('fecha__year', 'fecha__month')
            )
            print(f"Resultados de horas por mes: {horas_por_mes}")

            if not horas_por_mes:
                return Response(
                    {'message': 'No se encontraron horas registradas para este usuario.'},
                    status=status.HTTP_200_OK
                )

            resultado = [
                {
                    'mes': f"{item['fecha__year']}-{item['fecha__month']:02d}",
                    'total_horas': item['total_horas']
                }
                for item in horas_por_mes
            ]

            return Response(resultado, status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:
            return Response(
                {'error': 'Usuario no encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            return Response(
                {'error': f'Error inesperado: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
