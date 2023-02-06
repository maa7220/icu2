# Generated by Django 4.1.5 on 2023-01-09 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_admin_doctor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_nurse', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
