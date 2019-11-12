# Generated by Django 2.2.5 on 2019-11-10 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0003_auto_20191018_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=512)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.AddField(
            model_name='stuff',
            name='acquire_time',
            field=models.DateTimeField(default='1900-01-01 00:00:00', help_text='物品获得时间'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stuff',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='StuffCategoryRelationship',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuff.Category')),
                ('stuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuff.Stuff')),
            ],
            options={
                'db_table': 'stuff_category_relationship',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='Stuffs',
            field=models.ManyToManyField(through='stuff.StuffCategoryRelationship', to='stuff.Stuff'),
        ),
    ]