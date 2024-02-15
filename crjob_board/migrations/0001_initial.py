# Generated by Django 5.0.1 on 2024-02-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=400)),
                ('requirements', models.TextField(max_length=150)),
                ('location', models.TextField(max_length=200)),
                ('Hours', models.CharField(max_length=50)),
                ('salary', models.FloatField(max_length=100)),
            ],
        ),
    ]