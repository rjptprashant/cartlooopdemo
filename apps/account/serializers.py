from rest_framework import serializers
from .models import Operator, Client


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'user_id', 'user_timezone_hour')


