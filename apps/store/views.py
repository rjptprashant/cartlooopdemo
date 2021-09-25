from django.db import models
from django.shortcuts import render
from .models import Store, DiscountCode
from rest_framework import viewsets
from .serializers import StoreSerializer, DiscountCodeSerializer


class StoreViewSet(viewsets.ModelViewSet):
    """
    Viewset for the conversation
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer



class DiscountCodeViewSet(viewsets.ModelViewSet):
    """
    Viewset for the conversation
    """
    queryset = DiscountCode.objects.all()
    serializer_class = DiscountCodeSerializer