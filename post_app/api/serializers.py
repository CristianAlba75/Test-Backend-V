from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post model
    """
    class Meta:
        model = Post
        fields = ["id", "created_at", "name", "content", "email", "likes", "dislikes"]
