from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from drf_bia_api.permissions import IsOwnerOrReadOnly
from .models import Chef
from .serializers import ChefSerializer


class ChefList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = ChefSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Chef.objects.all().order_by('-created_at')

    filter_backends = [
        filters.SearchFilter
    ]

    search_fields = [
        'owner__username',
        'is_available',
        'location'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChefDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ChefSerializer
    queryset = Chef.objects.all().order_by('-created_at')