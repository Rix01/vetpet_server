from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    reservation_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Reservation
        fields = [
            'reservation_id',
            'user',
            'hospital',
            'pet',
            'reservation_date',
            'status'
        ]