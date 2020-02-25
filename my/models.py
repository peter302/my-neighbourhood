from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    occupants = models.PositiveIntegerField()
    health_contact = models.PositiveIntegerField()
    police_contact = models.PositiveIntegerField()
    hood_pic = models.ImageField(upload_to='images/', blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()
