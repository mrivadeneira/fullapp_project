# Generated by Django 3.1.7 on 2021-04-29 16:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20210427_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='movement_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 16, 31, 28, 785835, tzinfo=utc)),
        ),
    ]
