# Generated by Django 5.0.3 on 2024-04-01 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0005_scholarship_apply_alter_scholarship_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scholarship',
            old_name='apply',
            new_name='url',
        ),
    ]
