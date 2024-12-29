from django.urls import path
from . import views

urlpatterns = [
    path('service1/', views.route_request, name='route_request'),  # Esta es la ruta que esperas
]
