# Generated by Django 5.1 on 2024-11-15 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_branch_address_remove_branch_branch_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='address',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='contact_info',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='email_address',
        ),
    ]
