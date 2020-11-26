# Generated by Django 3.1.3 on 2020-11-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='company',
            field=models.TextField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.TextField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='title',
            field=models.TextField(default=None, max_length=255),
        ),
    ]
