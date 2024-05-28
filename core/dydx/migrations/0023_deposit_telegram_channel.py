# Generated by Django 3.2.23 on 2024-05-23 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dydx', '0022_positions_wallet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telegram_channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_telegram', models.CharField(max_length=255)),
                ('channel_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_telegram', models.CharField(max_length=255)),
                ('volume', models.FloatField()),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dydx.wallet')),
            ],
        ),
    ]
