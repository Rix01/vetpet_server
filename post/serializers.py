from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    post_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Post
        fields = [
            'post_id',
            'user',
            'category',
            'title',
            'content',
            'created_at',
            'updated_at',
            'view_count',
            'like_count'
        ]