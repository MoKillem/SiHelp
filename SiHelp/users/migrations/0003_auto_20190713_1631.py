# Generated by Django 2.2.1 on 2019-07-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190713_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tutor',
            field=models.BooleanField(default=False),
        ),
    ]
