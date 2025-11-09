from rest_framework import serializers
from .models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
   hospital_id = serializers.IntegerField(source='id', read_only=True)

   class Meta:
       model = Hospital
       fields = [
           'hospital_id',
           'name',
           'address',
           'phone_number',
           'description',
           'operating_hours',
           'speciality',
           'rating',
           'review_count',
           'site_url'
       ]