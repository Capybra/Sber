# Generated by Django 4.2.7 on 2023-11-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
