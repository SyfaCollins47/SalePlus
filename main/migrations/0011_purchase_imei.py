# Generated by Django 5.1 on 2024-11-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_employee_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='imei',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
