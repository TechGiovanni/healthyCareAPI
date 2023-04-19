from django.test import TestCase
# here import the model


class UserTest(TestCase):
    def test_get_user(self):
        item = 1
        itemstr = item

        self.assertEqual(itemstr, "Icecream: 80")


# To run the test:
# python3 manage.py test
