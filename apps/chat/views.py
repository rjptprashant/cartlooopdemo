from django.db import models
from django.shortcuts import render
from .models import Conversation, Chat
from rest_framework import viewsets
from .serializers import ConversationSerializer, ChatSerializer


class ConversionViewSet(viewsets.ModelViewSet):
    """
    Viewset for the conversation
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer



class ChatViewSet(viewsets.ModelViewSet):
    """
    Viewset for the conversation
    """
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer