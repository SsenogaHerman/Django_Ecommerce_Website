# Generated by Django 5.2.3 on 2025-07-07 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='adress',
            name='zip',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
