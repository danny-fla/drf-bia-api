from rest_framework import generics, permissions
from drf_bia_api.permissions import IsOwnerOrReadOnly
from .models import RecipeComment
from .serializers import RecipeCommentSerializer, RecipeCommentDetailSerializer


class RecipeCommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = RecipeCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = RecipeComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RecipeCommentDetailSerializer
    queryset = RecipeComment.objects.all()