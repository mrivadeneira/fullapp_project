# Generated by Django 3.1.7 on 2021-04-25 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'Category1'), (2, 'Category2'), (3, 'Category3')]),
        ),
        migrations.AlterField(
            model_name='stock',
            name='color',
            field=models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'Color1'), (2, 'Color2'), (3, 'Color3'), (4, 'Color4'), (5, 'Color5'), (6, 'Color6'), (7, 'Color7')]),
        ),
        migrations.AlterField(
            model_name='stock',
            name='movement',
            field=models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'inbound'), (2, 'outbound'), (3, 'lost'), (4, 'found'), (5, 'definitive_lost'), (6, 'repairing'), (7, 'repairing_reactivated')]),
        ),
        migrations.AlterField(
            model_name='stock',
            name='size',
            field=models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'Size1'), (2, 'Size2'), (3, 'Size3'), (4, 'Size4'), (5, 'Size5'), (6, 'Size6')]),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sku',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stock_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'N/A'), (1, 'Type1'), (2, 'Type2'), (3, 'Type3'), (4, 'Type4')]),
        ),
    ]