# Generated by Django 4.1.5 on 2023-01-09 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_doctor_user_doctor_added_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='added_by',
            new_name='admin',
        ),
    ]
