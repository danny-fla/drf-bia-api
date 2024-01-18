from django.db.models import Count
from rest_framework import generics, permissions, filters
from drf_bia_api.permissions import IsOwnerOrReadOnly
from .models import Quicksnap
from .serializers import QuicksnapSerializer


class QuicksnapList(generics.ListCreateAPIView):
    """
    List quicksnaps or create a quicksnap if logged in
    The perform_create method associates the quicksnap with the logged in user.
    """
    serializer_class = QuicksnapSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Quicksnap.objects.annotate(
        quicksnap_likes_count=Count('QuicksnapLikes', distinct=True),
        quicksnap_comments_count=Count('QuicksnapComments', distinct=True),
    ).order_by('-created_at')
    serializer_class = QuicksnapSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    
    search_fields = {
        'owner__username',
        'title',
    }

    ordering_fields = [
        'quicksnap_likes_count',
        'quicksnap_comments_count'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class QuicksnapDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a quicksnap and edit or delete it if you own it.
    """
    serializer_class = QuicksnapSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Quicksnap.objects.all()