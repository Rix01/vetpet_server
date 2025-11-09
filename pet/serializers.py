from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    pet_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model = Pet
        fields= [
            'pet_id',
            'user',
            'name',
            'age',
            'type',
            'diseases',
            'special_notes',
            'birth_date',
            'gender',
            'weight'
        ]