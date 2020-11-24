from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    "test API View"

    def get(self, request, format=None):
        "returns a list of apiview features"
        an_apiview = [
            'uses http methods as functions'
            'is similar to a traditional django view',
            'gives you the most control over app logic',
            'is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})