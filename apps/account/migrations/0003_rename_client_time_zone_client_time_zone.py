# Generated by Django 3.2.7 on 2021-09-23 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_client_client_time_zone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_time_zone',
            new_name='time_zone',
        ),
    ]
