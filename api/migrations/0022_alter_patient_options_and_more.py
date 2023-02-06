# Generated by Django 4.1.5 on 2023-01-27 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_user_specialization'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['-date_joined'], 'verbose_name': 'Patients', 'verbose_name_plural': 'Patients'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Specialization',
            new_name='specialization',
        ),
        migrations.AddField(
            model_name='patient',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]