# Generated by Django 5.1.1 on 2024-09-11 05:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0007_alter_plan_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
