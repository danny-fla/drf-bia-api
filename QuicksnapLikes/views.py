from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from drf_bia_api.permissions import IsOwnerOrReadOnly
from QuicksnapLikes.models import QuicksnapLike
from QuicksnapLikes.serializers import QuicksnapLikeSerializer

class QuicksnapLikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = QuicksnapLikeSerializer
    queryset = QuicksnapLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class QuicksnapLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = QuicksnapLikeSerializer
    queryset = QuicksnapLike.objects.all()

