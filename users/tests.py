import logging

from django.db import connection, reset_queries
from django.test import RequestFactory, TestCase
from django.test.utils import override_settings
from rest_framework import status

from users.models import User
from users.views_v1 import UserView


logger = logging.getLogger(__name__)

def log_queries():    
    logger.info("QUERIES COUNT: " + str(len(connection.queries)))
    for query in connection.queries:
        logger.info("----------------------------------------------------------------------\n" + query['sql'])
    reset_queries()


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


class ApiTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    @override_settings(DEBUG=True)
    def test_api_user(self):

        payload = {
            "email": "api_test@email.com",
            "first_name": "First Name",
            "last_name": "Last Name",
            "phone": "111 22 333 4444",
            "hobbies": [
                "Football",
                "Numismatics",
                "Videogames",
                ]
        }

        request = self.factory.post("/api/v1/signup/", data=payload, content_type="application/json")
        response = UserView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        log_queries()

        user_email = "api_test@email.com"
        request = self.factory.get(f"/api/v1/profile/{user_email}")
        response = UserView.as_view()(request, user_email)
        self.assertEqual(response.data["first_name"], "First Name")
        self.assertEqual(response.data["last_name"], "Last Name")
        self.assertEqual(response.data["phone"], "111 22 333 4444")
        self.assertListEqual(response.data["hobbies"], list(["Football", "Numismatics", "Videogames"]))
        self.assertFalse(response.data["is_valid_email"])
        self.assertFalse(response.data["is_valid_phone"])

        log_queries()
