# Generated by Django 3.1.4 on 2020-12-06 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0011_yarn_care_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yarn',
            name='care_instructions',
            field=models.CharField(default='', max_length=500),
        ),
    ]
