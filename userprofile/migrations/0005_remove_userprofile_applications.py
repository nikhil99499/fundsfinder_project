# Generated by Django 5.0.2 on 2024-02-13 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_userprofile_applications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='applications',
        ),
    ]
