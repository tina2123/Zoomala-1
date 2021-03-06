# Generated by Django 2.1.15 on 2020-05-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_image'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['bio'], name='bio_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['location'], name='profile_location_idx'),
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['-timestamp'], name='prof_time_desc_idx'),
        ),
    ]
