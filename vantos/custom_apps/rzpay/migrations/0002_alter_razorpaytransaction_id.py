# Generated by Django 3.2.6 on 2021-12-11 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rzpay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='razorpaytransaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
