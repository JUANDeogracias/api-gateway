from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def get_all_users(self, request):
        users = User.objects.all()
        if not users:

            return Response({'message':'no hay usuarios hasta el momento'},
                            status=status.HTTP_200_OK)


        return Response({'message':'no hay usuarios hasta el momento'},
                            status=status.HTTP_200_OK)
