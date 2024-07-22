from django.contrib.auth.models import User
from django.db import models


class Transaction(models.Model):
    transaction_type = [
        ('expense', 'expense'),
        ('income', 'income')
    ]
    type = models.CharField(choices=transaction_type, max_length=20)
    description = models.CharField(max_length=255, verbose_name='توضیحات')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    amount = models.BigIntegerField(verbose_name='مقدار')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return '{}-{}-{}'.format(self.date, self.user, self.amount)

    class Meta:
        verbose_name = 'تراکنش'
        verbose_name_plural = 'تراکنش ها'
