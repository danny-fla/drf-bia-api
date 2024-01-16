from rest_framework import serializers
from QuicksnapLikes.models import QuicksnapLike


class QuicksnapLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the QuicksnapLike model
    The create method handles the unique constraint on 'owner' and 'quicksnap'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = QuicksnapLike
        fields = ['id', 'created_at', 'owner', 'quicksnap']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })