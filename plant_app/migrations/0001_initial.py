# Generated by Django 4.2.1 on 2023-05-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phn', models.IntegerField()),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
