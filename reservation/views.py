from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Reservation
from .serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        # 예약 관련 모든 작업은 인증된 사용자만 가능
        permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]