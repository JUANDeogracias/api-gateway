import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def route_request(request):
    service_map = {
        'GET': {
            '/api/service1/': 'http://localhost:8001/api/users/get_all_users/',
        },
        'POST': {
            '/api/service1/': 'http://localhost:8001/api/users/add_user/',
        },
    }

    method = request.method.upper()
    if method in service_map:
        for route_prefix, service_url in service_map[method].items():
            if request.path.startswith(route_prefix):
                # Construye la URL de destino del microservicio
                target_url = service_url + request.path[len(route_prefix):]
                print(f"Redirecting to: {target_url}")

                try:
                    # Redirige la solicitud al microservicio
                    response = requests.request(
                        method=request.method,
                        url=target_url,
                        headers=request.headers,
                        data=request.body
                    )

                    # Intenta convertir la respuesta en JSON
                    try:
                        json_response = response.json()
                    except ValueError:
                        return JsonResponse({'error': 'Invalid JSON response from microservice'}, status=500)

                    return JsonResponse(json_response, status=response.status_code)

                except requests.exceptions.RequestException as e:
                    return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Route not found or method not supported'}, status=404)
