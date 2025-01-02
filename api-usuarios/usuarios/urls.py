from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .Views import UserView
from rest_framework.routers import DefaultRouter


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .Views.UserView import UserViewSet
from .Views.HorasView import HorasViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'horas', HorasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]