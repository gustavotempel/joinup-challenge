from django.test import TestCase

from users.models import User


class UserModelTestCase(TestCase):

    def setUp(self):
        pass

    def test_create_user(self):

        User.objects.create(
            email = "test@email.com",
            first_name = "First Name",
            last_name = "Last Name",
            phone = "111 22 333 4444",
            hobbies = list([
                "Football",
                "Numismatics",
                "Videogames",
                ]
            ),
        )

        test_user = User.objects.get(email="test@email.com")

        self.assertEqual(test_user.first_name, "First Name")
        self.assertEqual(test_user.last_name, "Last Name")
        self.assertEqual(test_user.phone, "111 22 333 4444")
        self.assertListEqual(test_user.hobbies, list(["Football", "Numismatics", "Videogames", ]))
        self.assertIsNone(test_user.email_validated_at)
        self.assertIsNone(test_user.phone_validated_at)
