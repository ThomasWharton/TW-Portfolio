# Generated by Django 4.2.5 on 2023-09-18 14:19

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('main_heading', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_heading', models.CharField(blank=True, max_length=100, null=True)),
                ('brief_description', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('detail_paragraph_1', models.CharField(blank=True, max_length=800, null=True)),
                ('detail_paragraph_2', models.CharField(blank=True, max_length=800, null=True)),
                ('detail_paragraph_3', models.CharField(blank=True, max_length=800, null=True)),
                ('full_name', models.CharField(max_length=150)),
                ('nationality', models.CharField(max_length=150)),
                ('nationality_flag', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('studying', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('project_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('project_description', models.CharField(blank=True, max_length=400, null=True)),
                ('site_link', models.URLField()),
                ('repo_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('skill_icon', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('skill_description', models.CharField(blank=True, max_length=400, null=True)),
                ('skill_competency', models.CharField(blank=True, max_length=400, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tw_portfolio.skillcategory')),
            ],
        ),
    ]
