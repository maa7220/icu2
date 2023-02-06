from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
import uuid
from phonenumber_field.modelfields import PhoneNumberField
User = settings.AUTH_USER_MODEL


# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


# Create your models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, username, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, username, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, username, password,  **extra_fields)

    def create_superuser(self, email, password, username, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, username, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=254)
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = PhoneNumberField(null=True)
    role = models.CharField(max_length=30)
    specialization = models.CharField(max_length=300)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)

    added_by = models.ForeignKey('self', models.CASCADE, null=True, blank=True)

    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=3, blank=True, null=True)
    nat_id = models.IntegerField()
    date_joined = models.DateTimeField(default=timezone.now)

    otp = models.CharField(max_length=4, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # this field we inherit from PermissionsMixin.
    is_superuser = models.BooleanField(default=False)

    is_doctor = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
        db_table = u'Users'
        ordering = ['-date_joined']

    def __str__(self):
        return self.username


# Create Auth Token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# password_reset_token_created
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{} ?code={}".format(
        reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset",
        # message:
        email_plaintext_message,
        # from:
        "ma722072207220@gmail.com",
        # to:
        [reset_password_token.user.email]
    )


# Admin Class
class Admin(models.Model):
    user = models.OneToOneField(
        User, related_name='users_admin', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admin'
        db_table = u'Admin'

    def __str__(self):
        return self.user.username


class Nurse(models.Model):
    user = models.OneToOneField(
        User, related_name='users_nurse', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    user = models.OneToOneField(
        User, related_name='users_doctor', on_delete=models.CASCADE)

    nurse = models.ManyToManyField(
        Nurse, related_name='doctor_nurse')

    def __str__(self):
        return self.user.username


# Patient
class Patient(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    name = models.CharField(max_length=220)
    age = models.IntegerField()
    gender = models.CharField(max_length=7)
    status = models.CharField(max_length=150)

    nat_id = models.IntegerField()
    room_number = models.IntegerField()
    disease_type = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    date_joined = models.DateTimeField(default=timezone.now)

    added_by = models.ForeignKey(
        Admin, related_name='added_admin', on_delete=models.CASCADE)

    doctor = models.ManyToManyField(
        Doctor,
        related_name='doctor'
    )
    nurse = models.ManyToManyField(
        Nurse,
        related_name='nurse'
    )

    class Meta:
        verbose_name = 'Patients'
        verbose_name_plural = 'Patients'
        db_table = u'Patients'

        ordering = ['-date_joined']

    def __str__(self):
        return self.name
