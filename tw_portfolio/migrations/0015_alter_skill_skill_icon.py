# Generated by Django 4.2.5 on 2025-03-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tw_portfolio', '0014_personaldetail_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_icon',
            field=models.URLField(blank=True, max_length=120, null=True),
        ),
    ]
