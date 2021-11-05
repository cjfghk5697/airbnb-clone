from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    '''
    Custom User Model
    '''
    GENDER_MALE="male"
    GENDER_FEMALE="female"
    GENDER_OTHER="other"
    GENDER_CHOICES=(
        (GENDER_MALE,"Male"),
        (GENDER_FEMALE,"Female"),
        (GENDER_OTHER,"Other"),
    )
    avatar=models.ImageField(null=True,blank=True)
    gender=models.CharField(
        choices=GENDER_CHOICES,max_length=10, null=True,blank=True
    )

    LANGUAGE_ENGLISH="english"
    LANGUAGE_KOREAN="korean"

    LANGUAGE_CHOICES=(
        (LANGUAGE_ENGLISH,"English"),
        (LANGUAGE_KOREAN,"Korean")
    )

    CURRENCY_USD="usd"
    CURRENCY_KRW="krw"
    CURRRENCHY_CHOICES=(
        (CURRENCY_USD,"USD"),
        (CURRENCY_KRW,"KRW")
    )


    bio = models.TextField(default="",blank=True)
    birthday=models.DateField(null=True)
    langauae=models.CharField(choices=LANGUAGE_CHOICES,max_length=2,null=True,blank=True)
    currency=models.CharField(choices=CURRRENCHY_CHOICES,max_length=3, null=True, blank=True)
    superhost=models.BooleanField(default=False)