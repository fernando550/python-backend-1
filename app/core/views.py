from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, viewsets

from core import serializers, models, permissions


class HelloApiView(APIView):
    "test API View"
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        "returns a list of apiview features"
        an_apiview = [
            'uses http methods as functions'
            'is similar to a traditional django view',
            'gives you the most control over app logic',
            'is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        "create a hello message with our name"
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        "handle updating an object"
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        "handle partial update of an object"
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        "delete an object"
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    "test API ViewSet"
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        "return a hello message"
        a_viewset = [
            'uses actions (list, create, retrieve, update, partial_update',
            'automatically maps to URLs using Routers',
            'provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        "create a new hello message"
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        "get an object by ID"
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        "update an object"
        return Response({'method': 'PUT'})

    def partial(self, request, pk=None):
        "partially ubdate an object"
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        "delete an object"
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    "handle creating and updating profiles"
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )