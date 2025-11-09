from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    comment_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Comment
        fields = [
            'comment_id',
            'user',
            'post',
            'parent_comment',
            'content',
            'created_at',
            'updated_at'
        ]