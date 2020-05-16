import time

from django.db import models

from common.models import City

from django.conf import settings

# Create your models here.


def upload_institution_image(instance, filename):
    last_dot = filename.rfind('.')
    extension = filename[last_dot:len(filename):1]
    return 'images/companies/%s-%s%s' % (instance.name, time.time(), extension)


class Institution(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255) #university or college
    address = models.CharField(max_length=255)
    website = models.URLField(max_length=200)
    image = models.FileField(upload_to=upload_institution_image, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)


class Faculty(models.Model):
    faculty = models.CharField(max_length=255)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=False, null=False)


class CareerCenter(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, blank=False, null=False)
    contact_person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)