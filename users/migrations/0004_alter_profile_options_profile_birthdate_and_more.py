# Generated by Django 4.2.7 on 2023-11-06 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_pincode_alter_profile_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(default='2000-01-01', verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='default@mail.ru', max_length=100, verbose_name='Адрес электронной почты'),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default='Иванович', max_length=50, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], default='М', max_length=1, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='profile',
            name='surname',
            field=models.CharField(default='Иванович', max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Иван', max_length=50, verbose_name='Имя'),
        ),
    ]
