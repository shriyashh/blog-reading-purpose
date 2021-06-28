# Generated by Django 3.2 on 2021-06-10 12:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postimage',
            field=models.ImageField(blank=True, upload_to='postimages/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 10, 18, 0, 59, 89280)),
        ),
    ]