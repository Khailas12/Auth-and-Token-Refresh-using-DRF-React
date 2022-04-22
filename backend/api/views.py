from rest_framework.response import Response
from rest_framework.decorators import api_view

# Customize token claim to add additional info to show while checking jwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',       # to submit username and pswd
        '/api/token/refresh'       # new token based on the refresh token sent to the backend
    ]
    return Response(routes)
