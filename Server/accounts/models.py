from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Schedule(models.Model):
    schedule_name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Receipt(models.Model):
    total = models.IntegerField()
    date = models.DateField()
    place = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    country = models.CharField(max_length = 20)
    event = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class Expenditure(models.Model):
    specific_date = models.DateField()
    specific_place = models.CharField(max_length = 50)
    spent = models.IntegerField()
    exchange = models.IntegerField()
    accumulate = models.IntegerField()
    origin = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class ExchangeRates(models.Model):
    select_date = models.DateField(primary_key=True)
    # 국가명 저장을 원하는 거임? / 아님 해당 국가 그 날 환율을 DB에 저장할 거임?
    # American = models.IntegerField()