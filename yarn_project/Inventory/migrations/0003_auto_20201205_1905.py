# Generated by Django 3.1.4 on 2020-12-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_yarn_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='hook',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='project',
            name='pattern',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='project',
            name='recipient',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='yarn',
            field=models.ManyToManyField(blank=True, null=True, to='Inventory.Yarn'),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='grams',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]