# Generated by Django 3.2 on 2021-06-10 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0013_alter_post_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 10, 19, 46, 26, 22150)),
        ),
    ]
