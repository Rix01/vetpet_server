from rest_framework import serializers
from .models import PostImage

class PostImageSerializer(serializers.ModelSerializer):
    post_img_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = PostImage
        fields = [
            'post_img_id',
            'post',
            'post_img_url'
        ]