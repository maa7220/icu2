# Generated by Django 4.1.5 on 2023-01-10 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_nurse'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='nurse',
            field=models.ManyToManyField(null=True, related_name='doctor_nurse', to='api.nurse'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users_doctor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nurse',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users_nurse', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
