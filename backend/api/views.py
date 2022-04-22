from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',       # to submit username and pswd
        '/api/token/refresh'       # new token based on the refresh token sent to the backend
    ]
    return Response(routes)