import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def route_request(request):
    # Mapeo de servicios con la ruta correcta del microservicio
    service_map = {
        '/api/service1/': 'http://localhost:8001/api/users/get_all_users/',  # Redirige a /api/users/ en el microservicio
    }

    # Revisa si la URL solicitada coincide con alguna de las rutas definidas
    for route_prefix, service_url in service_map.items():
        if request.path.startswith(route_prefix):
            # Construye la URL del microservicio
            target_url = service_url + request.path[len(route_prefix):]

            # Imprime la URL para diagnosticar
            print(f"Redirecting to: {target_url}")

            # Redirige la solicitud al microservicio
            try:
                response = requests.request(
                    method=request.method,
                    url=target_url,
                    headers=request.headers,
                    data=request.body
                )

                # Intenta parsear la respuesta a JSON
                try:
                    json_response = response.json()
                except ValueError:  # Si la respuesta no es JSON
                    return JsonResponse({'error': 'Invalid JSON response from microservice'}, status=500)

                # Retorna la respuesta del microservicio
                return JsonResponse(json_response, status=response.status_code)

            except requests.exceptions.RequestException as e:
                # Si hay un error en la solicitud al microservicio
                return JsonResponse({'error': str(e)}, status=500)

    # Si no se encuentra la ruta
    return JsonResponse({'error': 'Route not found'}, status=404)
