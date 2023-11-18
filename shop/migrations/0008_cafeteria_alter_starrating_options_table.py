# Generated by Django 4.2.7 on 2023-11-16 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_star_rating_starrating_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafeteria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('address', models.CharField(db_index=True, max_length=100)),
                ('available', models.BooleanField(default=True)),
                ('rows', models.IntegerField(default=6)),
                ('cols', models.IntegerField(default=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Столовая',
                'verbose_name_plural': 'Столовые',
                'ordering': ('id',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.AlterModelOptions(
            name='starrating',
            options={'ordering': ('product_id',), 'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтинги'},
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('hidden', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
                ('order', models.TimeField(blank=True)),
                ('cafeteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cafeteria')),
            ],
            options={
                'verbose_name': 'Стол',
                'verbose_name_plural': 'Столы',
                'ordering': ('cafeteria_id', 'row', 'col'),
            },
        ),
    ]
