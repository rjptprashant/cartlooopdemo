# Generated by Django 3.2.7 on 2021-09-25 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210923_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='schedule_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('in-progress', 'In Progress'), ('finish', 'Finish')], default='created', max_length=12),
        ),
        migrations.AddField(
            model_name='schedule',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
