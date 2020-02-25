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

        @classmethod
    def find_neigborhood(cls, neigborhood_id):
        hood= cls.objects.get(id=neigborhood_id)
        return hood

    @classmethod
    def update_neighborhood(cls,id,name):
        cls.objects.filter(pk = id).update(name=name)
        new_name_object = cls.objects.get(name = name)
        new_name = new_name_object.name
        return new_name

    @classmethod
    def update_occupants(cls,id,occupants):
        cls.objects.filter(pk = id).update(occupants=occupants)
        new_occupants_object = cls.objects.get(pk__id=id)
        new_occupants = new_name_object.occupants
        return new_occupants

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True, blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True)
    profile_pic = models.ImageField(upload_to='images/', blank=True)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.name
