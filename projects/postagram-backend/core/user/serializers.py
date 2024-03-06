from core.abstract.serializers import AbstractSerializer
from core.user.models import User
from rest_framework import serializers
from django.conf import settings


class UserSerializer(AbstractSerializer):

    posts_count = serializers.SerializerMethodField()

    def get_posts_count(self, instance):
        return instance.post_set.all().count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        print("Test reg: ", representation['id'])
        if not representation['avatar']:
            representation['avatar'] = settings.DEFAULT_AVATAR_URL
            return representation
        if settings.DEBUG:
            request = self.context.get('request')
            representation['avatar'] = request.build_absolute_uri(representation['avatar'])
        return representation

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "is_active",
            "created",
            "updated",
            "posts_count",
        ]
        read_only_field = ["is_active"]
