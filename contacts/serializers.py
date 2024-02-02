from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model

    """
    owner = serializers.ReadOnlyField(source="owner.username")
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        """
        Returns a human readable time since the
        comment was created
        eg. '2 days ago'
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Returns a human readable time since the
        contact was updated
        eg. '15 minutes ago'
        """
        return naturaltime(obj.updated_at)

    class Meta:
        """
        Lists all the filds to be included in
        the data returned by this api
        """
        model = Contact
        fields = [
            "id",
            "owner",
            "reason",
            "content",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
        ]