import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def route_request(request):
    service_map = {
        '/api/service1/': 'http://localhost:8001/api/users/get_all_users/',
    }

    for route_prefix, service_url in service_map.items():
        if request.path.startswith(route_prefix):
            target_url = service_url + request.path[len(route_prefix):]
            print(f"Redirecting to: {target_url}")

            try:
                response = requests.request(
                    method=request.method,
                    url=target_url,
                    headers=request.headers,
                    data=request.body
                )

                try:
                    json_response = response.json()
                except ValueError:
                    return JsonResponse({'error': 'Invalid JSON response from microservice'}, status=500)

                return JsonResponse(json_response, status=response.status_code)

            except requests.exceptions.RequestException as e:
                return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Route not found'}, status=404)
