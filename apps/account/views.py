from django.db import models
from django.shortcuts import render
from .models import Operator, Client
from rest_framework import viewsets
from .serializers import OperatorSerializer, ClientSerializer


class OperatorViewSet(viewsets.ModelViewSet):
    """
    Viewset for the conversation
    """
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer



class ClientViewSet(viewsets.ModelViewSet):
    """
    Viewset for the conversation
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer