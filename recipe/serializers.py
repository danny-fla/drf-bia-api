from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Recipe
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',  'created_at',
            'updated_at', 'title', 'ingredients', 'profile_image',
            'instructions', 'duration', 'image', 'is_owner'
        ]
