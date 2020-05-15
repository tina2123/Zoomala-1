# Generated by Django 2.1.15 on 2020-05-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20200108_2040'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='tweet',
            index=models.Index(fields=['content'], name='content_idx'),
        ),
        migrations.AddIndex(
            model_name='tweet',
            index=models.Index(fields=['-timestamp'], name='tweet_time_desc_idx'),
        ),
    ]
