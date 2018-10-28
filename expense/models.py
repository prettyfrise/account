from django.db import models

# 날짜, 대분류, 소분류, 상세, 금액, 지불방식, 비고
# Create your models here.
class Expense_list(models.Model):
    usedate = models.DateField('date published')
    category = models.CharField(max_length=30)
    field = models.CharField(max_length=30)
    subscribe = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    payment_logic = models.CharField(max_length=30)
    etc = models.CharField(max_length=100)

