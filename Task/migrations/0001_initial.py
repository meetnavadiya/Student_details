# Generated by Django 5.1.3 on 2024-12-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('roll_no', models.IntegerField()),
                ('course', models.CharField(max_length=255)),
                ('address', models.TextField()),
            ],
        ),
    ]