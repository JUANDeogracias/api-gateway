from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Usuario
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer = UserSerializer

    @action(detail=False, methods=['get'])
    def get_all_users(self, request):
        #Obtenemos todos los usuarios y devolvemos una respuesta serializada a json en funcion de el contenido
        users = Usuario.objects.all()
        if not users:
            return Response({'message':'no hay usuarios. Api gateway funcionando perfectamente'},
                            status=status.HTTP_200_OK)


        serializer = UserSerializer(users, many=True)
        return Response({'users:':serializer.data},
                            status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def add_user(self, request):
        # .strip() permite eliminar los espacios
        content = {
            'nombre': request.data.get('nombre', '').strip(),
            'email': request.data.get('email', '').strip(),
            'primer_apellido': request.data.get('primer_apellido', '').strip(),
            'segundo_apellido': request.data.get('segundo_apellido', '').strip(),
        }

        # Verifica que los campos requeridos estén llenos
        if not content['nombre'] or not content['email']:
            return Response(
                {'error': 'Los campos "nombre" y "email" son obligatorios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Crea un nuevo usuario
            usuario = Usuario.objects.create(
                nombre=content['nombre'],
                email=content['email'],
                primer_apellido=content.get('primer_apellido', None),
                segundo_apellido=content.get('segundo_apellido', None),
            )
            return Response(
                {'exitoso': f'Usuario "{usuario.nombre}" creado correctamente.'},
                status=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            # Captura errores de validación
            return Response(
                {'error': f'Error de validación: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            # Captura otros errores
            return Response(
                {'error': f'Ocurrió un error al crear el usuario: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )