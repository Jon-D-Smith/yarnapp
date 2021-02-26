# Generated by Django 3.1.4 on 2020-12-03 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='project/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Yarn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='yarn/images/')),
                ('color', models.CharField(max_length=200)),
                ('weight', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], default='4', max_length=20)),
                ('brand', models.CharField(max_length=200)),
                ('yards', models.IntegerField()),
                ('hook', models.CharField(max_length=200)),
                ('grams', models.IntegerField()),
            ],
        ),
    ]
