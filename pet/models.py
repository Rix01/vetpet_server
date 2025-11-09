from django.db import models
from user.models import User

class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    type = models.CharField(max_length=30, null=False)
    diseases = models.CharField(max_length=100, null=True)
    special_notes = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    def __str__(self):
        return self.name
