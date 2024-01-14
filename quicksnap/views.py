from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Quicksnap
from .serializers import QuicksnapSerializer


class QuicksnapList(APIView):
    serializer_class = QuicksnapSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        quicksnaps = Quicksnap.objects.all()
        serializer = QuicksnapSerializer(
            quicksnaps, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = QuicksnapSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )