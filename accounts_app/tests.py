from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class UserTestCase(TestCase): #conducting tests on the User model
    
    def setUp(self):
        user = User.objects.create_user(username='tonny', password='123')

    def test_user_created(self):
        count_users = User.objects.count()
        print('the total number of users', count_users)
        self.assertEqual(count_users, 1)
