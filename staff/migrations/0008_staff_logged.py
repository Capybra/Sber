# Generated by Django 4.2.7 on 2023-11-22 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0007_remove_staff_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='logged',
            field=models.BooleanField(default=False),
        ),
    ]
