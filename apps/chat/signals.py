from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Chat, Schedule
from .tasks import send_alerts
from .utils import get_from_user_type, get_to_user_id, get_timezone_hour, get_schedule_hour_count


@receiver(post_save, sender=Chat) 
def create_profile(sender, instance, created, **kwargs):
    """
    signal to create record and celery sending alerts
    """
    if created:
        from_user_type = get_from_user_type(instance)
        timezone_hour = get_timezone_hour(instance, from_user_type)
        if timezone_hour >= settings.LOWER_TIMEZONE_HOUR or timezone_hour <= settings.HIGHER_TIMEZONE_HOUR:
            # Check if hour count is achieved or not
            per_hour_chat_count = get_schedule_hour_count()
            if per_hour_chat_count < settings.MAX_HOUR_CHAT_LIMIT:
                to_user_id = get_to_user_id(instance, from_user_type)
                # create schedule record for user alerts in the conversation
                Schedule.objects.create(
                            chat=instance,
                            from_user_id=to_user_id,
                            to_user_id=to_user_id
                        )
                # To send scheduled notification to the conversation users
                send_alerts.delay(instance.id)
            else:
                print('Per hour max limit reached')
        else:
            # can be stored as logged this event for future reference
            print('Out of timezoen')
        