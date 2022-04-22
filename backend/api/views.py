from django.http import JsonResponse
from rest_framework.response import Response


def getRoutes(request):
    routes = [
        '/api/token',       # to submit username and pswd
        '/api/token/refresh'       # new token based on the refresh token sent to the backend
    ]
    return JsonResponse(routes, safe=False)