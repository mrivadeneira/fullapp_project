# Generated by Django 3.1.7 on 2021-04-29 16:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20210429_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='movement_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
