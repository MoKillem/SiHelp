# Generated by Django 2.2.1 on 2019-06-22 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='download.jfif', upload_to='profile_pic'),
        ),
    ]