# Generated by Django 3.2 on 2021-06-16 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=150)),
                ('mname', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('address', models.TextField(max_length=150)),
                ('mobile', models.IntegerField()),
                ('subject', models.TextField(max_length=150)),
                ('message', models.CharField(max_length=150)),
            ],
        ),
    ]
