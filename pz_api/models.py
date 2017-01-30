import uuid

from django.db import models
from django.contrib.auth.models import User


class BankAccount(models.Model):
    """
    Info about a bank account.

    :param uuid id: UUID
    :param User user: user
    :param str name: name.
    :param str description: description.
    :param decimal balance: balance.
    :param str currency: currency.
    :param date created_at: date of creation.
    :param date updated_at: date of the last update.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def complex_str(self):
        if name.startswith('t'):
            if name[1] in 'aeiou':
                return self.name[:1]
            else:
                return ''
        elif name.startswith('p'):
            if name[1] in 'aeiou':
                return self.name[:1]
            else:
                return ''

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Info about a category.

    :param uuid id: UUID.
    :param User user: user.
    :param Category parent: parent category.
    :param str name: name.
    :param URLField icon: icon path.
    :param binary type: type of category (input/output).
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    icon = models.URLField()
    type = models.BinaryField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """
    Info about a transaction.

    :param uuid id: UUID.
    :param BankAccount bank_account: id of bank account.
    :param Category category: category.
    :param decimal amount: amount.
    :param date created_at: date of creation.
    :param date updated_at: date of the last update.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
