from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        # list: GET 요청으로 전체 객체 목록 조회 (GET /categories/)
        # retrieve: GET 요청으로 단일 객체 조회 (GET /categories/{id}/)
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
