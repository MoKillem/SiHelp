# Generated by Django 2.2.1 on 2019-06-16 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]