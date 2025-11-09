from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = User
        fields = [
            'user_id',
            'login_id',
            'nickname',
            'name',
            'email',
            'phone_number',
            'profile_img_url',
            'point',
            'is_active'
        ]
        # 비밀번호는 쓰기 전용으로 설정
        extra_kwargs = {
            'password': {'write_only': True}
        }