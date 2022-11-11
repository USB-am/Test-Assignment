# Generated by Django 3.2.7 on 2022-11-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ф.И.О. участника')),
                ('institution', models.CharField(max_length=255, verbose_name='Учебное заведение')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
                'ordering': ['name'],
            },
        ),
    ]
