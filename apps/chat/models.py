from django.db import models
from django.contrib.auth.models import User
from apps.account.models import Client, Operator
from apps.store.models import Store, DiscountCode
from .constants import CONVERSATION_STATUS ,CHAT_STATUS, SCHEDULE_STATUS


class Conversation(models.Model):
    """
    Model for conversation
    """
    store = models.ForeignKey(Store, models.CASCADE, related_name="store_conversations")
    client = models.ForeignKey(Client, models.CASCADE, related_name="client_conversations")
    operator = models.ForeignKey(Operator, models.CASCADE, related_name="operator_conversations")
    status = models.CharField(choices=CONVERSATION_STATUS, max_length=12, default='started')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Chat(models.Model):
    """
    Model for conversation chats
    """
    conversation = models.ForeignKey(Conversation, models.CASCADE, related_name="conversation_chats")
    discount_code = models.ForeignKey(DiscountCode, models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, models.CASCADE, related_name="user_chats")
    payload = models.CharField(max_length=300)
    status = models.CharField(choices=CHAT_STATUS, max_length=10, default='new')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Schedule(models.Model):
    """
    Model for chats schedule
    """
    chat = models.ForeignKey(Chat, models.CASCADE, related_name="chat_schedule")
    from_user = models.ForeignKey(User, models.CASCADE, related_name='from_user_chat_schedule')
    to_user = models.ForeignKey(User, models.CASCADE, related_name='to_user_chat_schedule')
    status = models.CharField(choices=SCHEDULE_STATUS, max_length=12, default='created')
    schedule_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    
