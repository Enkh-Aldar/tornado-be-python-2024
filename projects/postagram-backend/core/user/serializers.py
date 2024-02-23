
from core.abstract.serializers import AbstractSerializer
from core.user.models import User
from rest_framework import serializers

class UserSerializer(AbstractSerializer):
    
    posts_count = serializers.SerializerMethodField()
    def get_posts_count(self, instance):
        return instance.post_set.all().count()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
            'last_name', 'email',
            'is_active', 'created', 'updated', 'posts_count']
        read_only_field = ['is_active']