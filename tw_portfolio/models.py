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


class Heading(models.Model):
    hero_image = CloudinaryField('image', null=True, blank=True)
    main_heading = models.CharField(max_length=100, null=True, blank=True)
    sub_heading = models.CharField(max_length=100, null=True, blank=True)
    brief_description = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.main_heading


class Project(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    project_image = CloudinaryField('image', null=True, blank=True)
    project_description = models.CharField(max_length=400, null=True, blank=True)
    site_link = models.URLField()
    repo_link = models.URLField()

    def __str__(self):
        return self.name
