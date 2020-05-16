import time

from django.db import models

from common.models import City, Industry

from django.conf import settings

# Create your models here.


def upload_company_image(instance, filename):
    last_dot = filename.rfind('.')
    extension = filename[last_dot:len(filename):1]
    return 'images/companies/%s-%s%s' % (instance.name, time.time(), extension)


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    website = models.URLField(max_length=200)
    image = models.FileField(upload_to=upload_company_image, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    contact_person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)


class CompanyIndustries(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, blank=False, null=False)


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    salary = models.CharField(max_length=255)
    contract_type = models.CharField(max_length=255)
    required_experience = models.CharField(max_length=255)
    duties = models.CharField(max_length=2000)
    requirements = models.CharField(max_length=2000)
    conditions = models.CharField(max_length=2000)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False)


class StudentVacancies(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=False, null=False)