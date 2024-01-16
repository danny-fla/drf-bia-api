from rest_framework import serializers
from RecipeLike.models import RecipeLike


class RecipeLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'recipe'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = RecipeLike
        fields = ['id', 'created_at', 'owner', 'recipe']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })