from rest_framework import serializers
from .models import User, Schedule, Receipt, ExchangeRates, Expenditure
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'nickname')


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = ('schedule_name',)

class ReceiptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Receipt
        fields = ('total', 'date', 'place')

class ExchangeRatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExchangeRates
        fields = ('select_date',)

class ExpenditureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expenditure
        fields = ('accumulate',)