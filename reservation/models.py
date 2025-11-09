from django.db import models
from user.models import User
from hospital.models import Hospital
from pet.models import Pet

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=False)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=False)
    reservation_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, null=False, default='NONE')

    def __str__(self):
        return f"Reservation {self.reservation_id}"

