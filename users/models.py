from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    LANGUAGE_ENGLISH = 'EN'
    LANGUAGE_THAI = 'TH'
    LANGUAGE_CHOICES = [
        (LANGUAGE_ENGLISH, 'EN'),
        (LANGUAGE_THAI, 'TH'),
    ]

    SEX_MALE = 'male'
    SEX_FEMALE = 'female'
    SEX_NA = 'na'
    SEX_CHOICES = [
        (SEX_MALE, 'Male'),
        (SEX_FEMALE, 'Female'),
        (SEX_NA, "Don't want to specify"),
    ]

    profile_picture = models.ImageField(null=True, blank=True)
    language_preference = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, default=LANGUAGE_ENGLISH)
    sex = models.CharField(choices=SEX_CHOICES, max_length=20, default=SEX_MALE)