# Generated by Django 3.2.23 on 2024-04-07 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('on_counter_billing', '0002_auto_20240406_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]
