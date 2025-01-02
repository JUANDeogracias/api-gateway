from django.urls import path, re_path
from . import views

urlpatterns = [
    # Captura cualquier ruta que comience con "service1/" o "service2/"
    re_path(r'^(?P<service_name>service[12]/.*)$', views.route_request, name='route_request'),
]