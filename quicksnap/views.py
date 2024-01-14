from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Quicksnap
from .serializers import QuicksnapSerializer
from drf_bia_api.permissions import IsOwnerOrReadOnly


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

class QuicksnapDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = QuicksnapSerializer

    def get_object(self, pk):
        try:
            quicksnap = Quicksnap.objects.get(pk=pk)
            self.check_object_permissions(self.request, quicksnap)
            return quicksnap
        except Quicksnap.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        quicksnap = self.get_object(pk)
        serializer = QuicksnapSerializer(
            quicksnap, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        quicksnap = self.get_object(pk)
        serializer = QuicksnapSerializer(
            quicksnap, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        quicksnap = self.get_object(pk)
        quicksnap.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )