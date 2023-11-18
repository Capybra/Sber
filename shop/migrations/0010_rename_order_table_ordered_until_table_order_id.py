# Generated by Django 4.2.7 on 2023-11-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_table_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='order',
            new_name='ordered_until',
        ),
        migrations.AddField(
            model_name='table',
            name='order_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]