# Generated by Django 3.2.23 on 2024-05-25 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dydx', '0034_alter_staking_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staking',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
