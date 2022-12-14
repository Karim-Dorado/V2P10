from django.db import models
from django.contrib.auth.models import (
                                    AbstractBaseUser,
                                    BaseUserManager,
                                    PermissionsMixin
                                    )


class UserManager(BaseUserManager):
    """
    Class that is used to manage a user.
    """

    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):
        """
        Function used to create and save a user.
        """
        if not username:
            raise ValueError("The given username is not valid")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        """
        This function uses _create_user() to create a user wich is not a superuser.
        """
        return self._create_user(
            username,
            email,
            password,
            is_active=True,
            is_staff=False,
            is_superuser=False,
            **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        """
        This function uses _create_user() to create a user wich is a superuser.
        """
        user = self._create_user(
            username,
            email,
            password,
            is_active=True,
            is_staff=True,
            is_superuser=True,
            **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model that represents a user.
    """

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username
