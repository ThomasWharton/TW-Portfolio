# Generated by Django 4.2.5 on 2023-09-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tw_portfolio', '0006_delete_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetail',
            name='residence',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]