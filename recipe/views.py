from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_bia_api.permissions import IsOwnerOrReadOnly
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    """
    List recipes or create a recipe if logged in
    The perform_create method associates the recipe with the logged in user.
    """
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Recipe.objects.annotate(
        recipes_likes_count=Count('RecipeLikes', distinct=True),
        recipe_comments_count=Count('RecipeComments', distinct=True),
    ).order_by('-created_at')
    serializer_class = RecipeSerializer

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'RecipeLikes__owner__profile',
        'owner__profile',
        'RecipeComments__owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'recipes_likes_count',
        'recipe_comments_count'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a recipe and edit or delete it if you own it.
    """
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recipe.objects.annotate(
        recipes_likes_count=Count('RecipeLikes', distinct=True),
        recipe_comments_count=Count('RecipeComments', distinct=True),
    ).order_by('-created_at')
    serializer_class = RecipeSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'recipes_likes_count',
        'recipe_comments_count'
    ]
