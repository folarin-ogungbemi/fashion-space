from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MyUserManager
from django_countries.fields import CountryField


class MyUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    business_name = models.CharField(max_length=254, null=False, blank=False)
    password = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    designer = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    location = CountryField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    website = models.URLField(max_length=1024, null=True, blank=True)
    linkedIn = models.URLField(max_length=1024, null=True, blank=True)
    youtube = models.URLField(max_length=1024, null=True, blank=True)
    instagram = models.URLField(max_length=1024, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.designer