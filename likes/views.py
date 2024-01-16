from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from drf_bia_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer

class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()




# class LikeRecipeList(generics.CreateAPIView):
#     """
#     Create a like for a recipe.
#     """
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = LikeSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user, quicksnap=None)


# class LikeQuicksnapList(generics.CreateAPIView):
#     """
#     Create a like for a quicksnap.
#     """
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = LikeSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user, recipe=None)


# class LikeList(generics.CreateAPIView):
#     """
#     Create a like for a recipe or a quicksnap.
#     """
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = LikeSerializer

#     def perform_create(self, serializer):
#         like_type = self.request.data.get('like_type', None)

#         if like_type not in ['recipe', 'quicksnap']:
#             return Response({'detail': 'Invalid like_type. Choose either "recipe" or "quicksnap".'},
#                             status=status.HTTP_400_BAD_REQUEST)

#         serializer.save(owner=self.request.user)

#         if like_type == 'recipe':
#             serializer.save(quicksnap=None)
#         else:
#             serializer.save(recipe=None)
