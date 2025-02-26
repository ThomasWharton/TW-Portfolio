# Generated by Django 4.2.5 on 2025-02-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tw_portfolio', '0010_remove_skill_skill_competency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='main_heading',
        ),
        migrations.AlterField(
            model_name='education',
            name='accreditation',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='place_of_study',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_icon',
            field=models.URLField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skillcategory',
            name='category',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
