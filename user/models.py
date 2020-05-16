import time

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phone_field import PhoneField

from career_center.models import Institution
from common.models import City, Industry


# Create your models here.
from user.managers import CustomUserManager


def upload_avatar(instance, filename):
    last_dot = filename.rfind('.')
    extension = filename[last_dot:len(filename):1]
    return 'images/users/%s-%s-%s%s' % (instance.first_name, instance.last_name, time.time(), extension)


def upload_resume(instance, filename):
    last_dot = filename.rfind('.')
    extension = filename[last_dot:len(filename):1]
    return 'files/resume/%s-%s-%s%s' % (instance.first_name, instance.last_name, time.time(), extension)


class UserRole(models.Model):
    role = models.CharField(max_length=255)


class CustomUser(AbstractUser):
    avatar = models.FileField(upload_to=upload_avatar, blank=True, null=True)
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    phone_number = PhoneField(blank=True, help_text='Contact phone number')

    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.email


class Resume(models.Model):
    date_of_birth = models.DateField(blank=True, null=True)
    citizenship = models.CharField(max_length=255)
    desired_position = models.CharField(max_length=255)
    working_experience = models.CharField(max_length=2000)
    education_degree = models.CharField(max_length=255)
    skills = models.CharField(max_length=2000)
    resume_file = models.FileField(upload_to=upload_resume, blank=True, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    main_industry = models.ForeignKey(Industry, on_delete=models.CASCADE, blank=True, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=True, null=True)


