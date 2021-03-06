from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    USER_GENDER_TYPE = (
        ("male", "Male"),
        ("female", "Female"),
        ("prefer_not_to_say", "Prefer not to say")
    )

    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    nick_name = models.CharField("nickname", max_length=23, blank=True, default="")
    birthday = models.DateField("birthday", null=True, blank=True)
    gender = models.CharField("gender", max_length=20, choices=USER_GENDER_TYPE, default="male")
    address = models.CharField("address", max_length=100, blank=True, default="")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100,
                              verbose_name="Avatar")

    class Meta:
        verbose_name = "User Info"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.owner.username


class EmailVerification(models.Model):
    """email verification code"""
    SEND_TYPE_OPTIONS = (
        ('register', 'register'),
        ('forget', 'forget')
    )

    code = models.CharField('Verification code', max_length=20)
    email = models.CharField('Email', max_length=35)
    send_type = models.CharField(choices=SEND_TYPE_OPTIONS, default='register', max_length=20)

    class Meta:
        verbose_name = 'Verification code'
        verbose_name_plural = 'Verification codes'

    def __str__(self):
        return self.code
