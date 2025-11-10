from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    # 모든 사용자 데이터를 쿼리셋으로 지정
    queryset = User.objects.all()

    # 사용자 데이터 직렬화를 위한 시리얼라이저 지정
    serializer_class = UserSerializer

    # 동작(액션)에 따라 동적으로 권한 설정
    def get_permissions(self):
        # create 작업은 모든 사용자에게 허용
        if self.action == 'create':
            permission_classes = [AllowAny]
        # 다른 모든 작업(조회, 수정, 삭제 등)은 인증된 사용자만 허용
        else:
            permission_classes = [IsAuthenticated]
        # 권한 클래스 인스턴스 반환
        return [permission() for permission in permission_classes]

    # 커스텀 회원가입 액션 정의
    # detail=False: 전체 객체 컬렉션에 대한 액션
    # methods=['post']: POST 메서드로만 접근 가능
    @action(detail=False, methods=['post'])
    def register(self, request):
        # 요청된 데이터로 시리얼라이저 인스턴스 생성
        serializer = self.get_serializer(data=request.data)

        # 데이터 유효성 검사 (유효하지 않으면 예외 발생)
        serializer.is_valid(raise_exception=True)

        # 객체 생성
        self.perform_create(serializer)

        # 응답 헤더 생성
        headers = self.get_success_headers(serializer.data)

        # 생성된 사용자 데이터와 201 상태 코드로 응답
        return Response(serializer.data, status=201, headers=headers)