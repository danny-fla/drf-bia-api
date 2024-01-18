from rest_framework import serializers
from .models import Quicksnap
from QuicksnapLikes.models import QuicksnapLike


class QuicksnapSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    quicksnap_like_id = serializers.SerializerMethodField()

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

    def get_quicksnap_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            quicksnap_like = QuicksnapLike.objects.filter(
                owner=user, quicksnap=obj
            ).first()
            return quicksnap_like.id if quicksnap_like else None
        return None

    class Meta:
        model = Quicksnap
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_at','updated_at', 'title', 'content', 'image',
            'city', 'location','quicksnap_like_id'
        ]