# Generated by Django 3.1.4 on 2020-12-06 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0010_auto_20201206_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='yarn',
            name='care_instructions',
            field=models.TextField(default=''),
        ),
    ]