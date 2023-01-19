# Generated by Django 4.1 on 2023-01-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
