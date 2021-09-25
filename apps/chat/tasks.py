from celery import shared_task
from .models import Conversation, Schedule, Chat

@shared_task(name="send_alerts")
def send_alerts(chat_id):
    message = str()
    try:
        # -------------- retrieve chat message fron schedule_id ------------------- #
        chatObj = Chat.objects.get(id=chat_id)
        message = chatObj.payload if chatObj else ''
        message = message.replace("{{ discount.discount_code }}", chatObj.discount_code.discount_code if chatObj.discount_code else '')
        message = message.replace("{{ operator.full_name }}", chatObj.conversation.operator.user.get_full_name() if chatObj.conversation else '')
        message = message.replace("{{ client.first_name }}", chatObj.conversation.client.user.get_short_name() if chatObj.conversation else '')
        # TODO: Send email/sms to the user with above message and update schedule status
        # Update chat status
        chatObj.status = 'sent'
        chatObj.save()
    except Exception as e:
        print(e)
        pass
    return message