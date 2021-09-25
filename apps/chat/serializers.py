from rest_framework import serializers
from .models import Conversation, Chat
from .constants import CHAT_MESSAGE_REGEX_PATTERN, ERROR_CHAT_LENGTH_MESSAGE, ERROR_CHAT_PATTERN_MESSAGE
import re


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = '__all__'

    def validate_payload(self, payload):
        if len(payload) > 300:
            raise serializers.ValidationError(ERROR_CHAT_LENGTH_MESSAGE)
        elif re.search(CHAT_MESSAGE_REGEX_PATTERN, payload):
            raise serializers.ValidationError(ERROR_CHAT_PATTERN_MESSAGE)
        return payload


class ConversationSerializer(serializers.ModelSerializer):
    chats = ChatSerializer(source='conversation_chats', many=True)
    class Meta:
        model = Conversation
        fields = ('id', 'store_id', 'operator_id', 'client_id', 'status', 'chats')


