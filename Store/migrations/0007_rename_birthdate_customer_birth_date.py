# Generated by Django 5.2.3 on 2025-07-08 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='birthdate',
            new_name='birth_date',
        ),
    ]
