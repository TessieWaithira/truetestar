from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Company(models.Model):
    company_name = models.CharField(max_length=200, unique=True)
    company_website = models.URLField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=200)


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=12)
    profile_image = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    interests = models.TextField(max_length=500, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Test(models.Model):
    project_name = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='images/')
    project_description = models.TextField(max_length=500)
    device_requirements = models.CharField(max_length=200, blank=True, null=True)
    location_of_testers = models.CharField(max_length=200)
    number_of_testers = models.CharField(max_length=200)
    expertise_level = models.CharField(max_length=200)
    test_instructions = models.TextField(max_length=500, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)


