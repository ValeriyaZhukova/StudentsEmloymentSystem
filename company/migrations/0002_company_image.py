# Generated by Django 2.2.5 on 2020-05-16 12:43

import company.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=company.models.upload_company_image),
        ),
    ]