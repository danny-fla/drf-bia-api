from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_bia_api.permissions import IsOwnerOrReadOnly
from .models import QuicksnapComment
from .serializers import QuicksnapCommentSerializer, QuicksnapCommentDetailSerializer


class QuicksnapCommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = QuicksnapCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = QuicksnapComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quicksnap']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class QuicksnapCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = QuicksnapCommentDetailSerializer
    queryset = QuicksnapComment.objects.all()