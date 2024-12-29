from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]