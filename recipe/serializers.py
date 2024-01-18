from rest_framework import serializers
from .models import Recipe
from RecipeLike.models import RecipeLike


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    recipe_like_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_recipe_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            recipe_like = RecipeLike.objects.filter(
                owner=user, recipe=obj
            ).first()
            return recipe_like.id if recipe_like else None
        return None

    class Meta:
        model = Recipe
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',  'created_at',
            'updated_at', 'title', 'ingredients', 'profile_image',
            'instructions', 'duration', 'image', 'recipe_like_id'
        ]
