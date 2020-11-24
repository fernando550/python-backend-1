from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core import serializers


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