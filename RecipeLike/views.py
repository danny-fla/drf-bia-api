from rest_framework import generics, permissions
from drf_bia_api.permissions import IsOwnerOrReadOnly
from RecipeLike.models import RecipeLike
from RecipeLike.serializers import RecipeLikeSerializer


class RecipeLikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RecipeLikeSerializer
    queryset = RecipeLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RecipeLikeSerializer
    queryset = RecipeLike.objects.all()
