# Generated by Django 3.2 on 2021-06-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_alter_post_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
