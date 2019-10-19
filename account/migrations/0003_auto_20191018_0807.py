# Generated by Django 2.2.5 on 2019-10-18 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191018_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('create_datetime', models.DateTimeField(auto_now=True)),
                ('update_datetime', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('create_datetime', models.DateTimeField(auto_now=True)),
                ('update_datetime', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('create_datetime', models.DateTimeField(auto_now=True)),
                ('update_datetime', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'gender',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('create_datetime', models.DateTimeField(auto_now=True)),
                ('update_datetime', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'province',
            },
        ),
        migrations.RemoveField(
            model_name='account',
            name='sexual_orientation',
        ),
        migrations.AlterField(
            model_name='account',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.City'),
        ),
        migrations.AlterField(
            model_name='account',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Country'),
        ),
        migrations.AlterField(
            model_name='account',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Province'),
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Gender'),
            preserve_default=False,
        ),
    ]