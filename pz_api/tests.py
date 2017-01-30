from django.contrib.auth.models import User
from django.test import TestCase

from .models import BankAccount
from .models import Category
from .models import Transaction


class APITestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('myname', 'mypassword')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_create_bacnk_account(self):
        name = 'test'
        ba = BankAccount(user=self.user,
                name=name,
                description='desc',
                balance=10,
                currency='EUR')
        ba.save()
        self.assertEqual(BankAccount.objects.count(), 1)
        self.assertEqual(BankAccount.objects.first().__str__(), name)
