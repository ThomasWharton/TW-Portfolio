from django.db import models
from django.contrib import admin
from cloudinary.models import CloudinaryField


class PersonalDetail(models.Model):
    detail_paragraph_1 = models.CharField(max_length=800, null=True, blank=True)
    detail_paragraph_2 = models.CharField(max_length=800, null=True, blank=True)
    full_name = models.CharField(max_length=150, unique=False)
    nationality = models.CharField(max_length=150, unique=False)
    nationality_flag = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.full_name


class Home(models.Model):
    hero_image = CloudinaryField('image', null=True, blank=True)
    main_heading = models.CharField(max_length=100, null=True, blank=True)
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


class SkillCategory(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.category


class Skill(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    skill_icon = CloudinaryField('image', null=True, blank=True)
    skill_description = models.CharField(max_length=400, null=True, blank=True)
    skill_competency = models.CharField(max_length=400, null=True, blank=True)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Social(models.Model):
    social_icon = models.CharField(max_length=50, null=True, blank=True)
    social_url = models.URLField()

    def __str__(self):
        return self.social_icon


class WorkHistory(models.Model):
    company_name = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.company_name


class Education(models.Model):
    place_of_study = models.CharField(max_length=150, null=True, blank=True)
    accreditation = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.place_of_study
