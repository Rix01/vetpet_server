from django.db import models

class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    description = models.TextField(null=False)
    operating_hours = models.JSONField(null=False)
    speciality = models.CharField(max_length=100, null=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    review_count = models.IntegerField(null=False, default=0)
    site_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name