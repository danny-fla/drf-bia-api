from rest_framework import serializers
from .models import QuicksnapComment


class QuicksnapCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the QuicksnapComments model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = QuicksnapComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'quicksnap', 'created_at', 'updated_at', 'content'
        ]

class QuicksnapCommentDetailSerializer(QuicksnapCommentSerializer):
    """
    Serializer for the QuicksnapComment model used in Detail view
    Quicksnap is a read only field so that we dont have to set it on each update
    """
    quicksnap = serializers.ReadOnlyField(source='quicksnap.id')