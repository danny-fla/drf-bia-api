from rest_framework import serializers
from .models import RecipeComment


class RecipeCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the RecipeComments model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = RecipeComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'recipe', 'created_at', 'updated_at', 'content'
        ]


class RecipeCommentDetailSerializer(RecipeCommentSerializer):
    """
    Serializer for the RecipeComment model used in Detail view
    Recipe is a read only field so that we dont have to set it on each update
    """
    recipe = serializers.ReadOnlyField(source='recipe.id')
