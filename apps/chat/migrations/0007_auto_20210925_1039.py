# Generated by Django 3.2.7 on 2021-09-25 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210923_0549'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0006_auto_20210925_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'Created'), ('in-progress', 'In Progress'), ('finish', 'Finish')], default='created', max_length=12)),
                ('schedule_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='discount_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.discountcode'),
        ),
        migrations.DeleteModel(
            name='ScheduleAlert',
        ),
        migrations.AddField(
            model_name='schedule',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_schedule', to='chat.chat'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user_chat_schedule', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schedule',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user_chat_schedule', to=settings.AUTH_USER_MODEL),
        ),
    ]
