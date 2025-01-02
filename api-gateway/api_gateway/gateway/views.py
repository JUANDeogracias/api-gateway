import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def route_request(request, service_name):
    """
    API Gateway para enrutar solicitudes basadas en rutas dinámicas.
    """
    service_map = {
        'GET': {
            'service1/': 'http://localhost:8001/api/users/get_all_users/',
            'service2/horas_por_mes/': 'http://localhost:8001/api/horas/horas_por_mes/',
        },
        'POST': {
            'service1/': 'http://localhost:8001/api/users/add_user/',
            'service2/horas/': 'http://localhost:8001/api/horas/add_horas/',
        },
    }

    method = request.method.upper()
    print(f"Method: {method}, Service Name: {service_name}")  # Registro adicional

    if method in service_map:
        for route_prefix, service_url in service_map[method].items():
            if service_name.startswith(route_prefix):
                # Construye la URL de destino del microservicio
                target_url = service_url
                print(f"Redirigiendo a: {target_url}")  # Registro adicional

                try:
                    # Redirige la solicitud al microservicio
                    response = requests.request(
                        method=request.method,
                        url=target_url,
                        headers={key: value for key, value in request.headers.items() if key != 'Host'},
                        data=request.body,
                        params=request.GET.dict()  # Incluye parámetros de consulta
                    )

                    print(f"Microservicio Respondió: {response.status_code}")  # Registro adicional

                    try:
                        json_response = response.json()
                    except ValueError:
                        return JsonResponse({'error': 'Respuesta inválida desde el microservicio.'}, status=500)

                    # Modificación aquí
                    return JsonResponse(json_response, status=response.status_code, safe=False)

                except requests.exceptions.RequestException as e:
                    return JsonResponse({'error': f'Error al conectar con el microservicio: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Ruta no encontrada o método no soportado.'}, status=404)
