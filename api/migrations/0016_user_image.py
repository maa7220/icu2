# Generated by Django 4.1.5 on 2023-01-14 19:39

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_rename_mobile_patient_phone_remove_patient_sick_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.upload_to),
        ),
    ]
