# Generated by Django 3.2.8 on 2021-11-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usefulModels', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='readingbook',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]