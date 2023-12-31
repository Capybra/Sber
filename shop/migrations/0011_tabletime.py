# Generated by Django 4.2.7 on 2023-11-19 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_order_table_ordered_until_table_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ordered_at', models.CharField(max_length=10)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.table')),
            ],
            options={
                'verbose_name': 'Время стола',
                'verbose_name_plural': 'Время столов',
                'ordering': ('table_id', 'ordered_at'),
            },
        ),
    ]
