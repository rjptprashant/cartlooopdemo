import datetime
from .models import Chat, Schedule


def get_from_user_type(instance):
    try:
        from_user_type = 'client' if instance.user.client else "operator"
    except:
        from_user_type = 'operator'
    return from_user_type


def get_to_user_id(instance, from_user_type):
    try:
        if from_user_type == 'client':
            to_user_id = instance.conversation.operator.user.id
        else:
            to_user_id = instance.conversation.client.user.id
    except:
        pass
    return to_user_id


def get_timezone_hour(instance, from_user_type):
    try:
        if from_user_type == 'client':
            timezone_hour = instance.conversation.client.user_timezone_hour
        else:
            timezone_hour = instance.conversation.store.store_timezone_hour
    except:
        pass
    return timezone_hour


def get_schedule_hour_count():
    try:
        return Schedule.objects.filter(
            schedule_date__date=datetime.datetime.now().strftime('%Y-%m-%d'),
            schedule_date__hour=datetime.datetime.now().hour).count()
    except Exception as e:
        print(e)
    return 0
    
    