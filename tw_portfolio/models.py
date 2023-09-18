from django.db import models
from django.contrib import admin
from cloudinary.models import CloudinaryField


class PersonalDetail(models.Model):
    profile_image = CloudinaryField('image', null=True, blank=True)
    detail_paragraph_1 = models.CharField(max_length=800, null=True, blank=True)
    detail_paragraph_2 = models.CharField(max_length=800, null=True, blank=True)
    detail_paragraph_3 = models.CharField(max_length=800, null=True, blank=True)
    full_name = models.CharField(max_length=150, unique=False)
    nationality = models.CharField(max_length=150, unique=False)
    nationality_flag = CloudinaryField('image', null=True, blank=True)
    studying = models.CharField(max_length=200, unique=False)

    def __str__(self):
        return self.full_name

