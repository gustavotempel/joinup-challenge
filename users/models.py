from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(AbstractUser):
    """ Custom User model extended from AbstractUser. """

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email_validated_at = models.DateTimeField(null=True, editable=False)
    phone_validated_at = models.DateTimeField(null=True, editable=False)
    hobbies = ArrayField(models.CharField(max_length=100), default=list())

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "last_name",
        "phone",
        ]
