# Generated by Django 4.1.5 on 2023-01-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Specialization',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
