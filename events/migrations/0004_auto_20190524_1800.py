# Generated by Django 2.2.1 on 2019-05-24 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190524_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='latitude',
            field=models.DecimalField(decimal_places=14, max_digits=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='longitude',
            field=models.DecimalField(decimal_places=14, max_digits=20),
        ),
    ]
