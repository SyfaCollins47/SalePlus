# Generated by Django 5.1 on 2024-11-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='price',
        ),
        migrations.AddField(
            model_name='purchase',
            name='total_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='unit_price',
            field=models.FloatField(null=True),
        ),
    ]
