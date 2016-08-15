from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):

    def _create_user(self,Username,password, **extra_fields):
        if not Username:
            raise ValueError('The given username must be set')
        username = Username
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username,password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    # id_char = models.(unique=True,blank=True)
    is_active = models.BooleanField(('active'), default=True)

class User_type_1(MyUser):
    username = models.CharField(max_length=10,unique=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''

        return self.username

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.username

class User_type_2(MyUser):
    email = models.EmailField(unique=True)
