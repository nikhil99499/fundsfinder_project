# Generated by Django 5.0.2 on 2024-03-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='eligibility_criteria',
            field=models.TextField(blank=True, null=True),
        ),
    ]
