# Generated by Django 2.2.5 on 2019-10-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191018_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=128),
        ),
    ]
