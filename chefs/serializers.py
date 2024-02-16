from rest_framework import serializers
from .models import Chef


class ChefSerializer(serializers.ModelSerializer):
    """
    Chef serializer to add the owners profile image.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    reviews_count = serializers.ReadOnlyField()
    average_rating = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        returns true if the user making the request
        is the owner of the chef object
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Lists all the filds to be included in
        the data returned by this api
        """
        model = Chef
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'profile_image', 'is_available', 'experience', 'location',
            'email', 'phone', 'created_at', 'updated_at',
            'reviews_count', 'average_rating',
        ]
