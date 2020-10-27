from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True)

    first_name = models.CharField('first name', max_length=30, blank=True)
    surname = models.CharField('surname', max_length=50, blank=True)
    id_no = models.IntegerField('id number', unique=True)
    # category - whether a patient , specialist or nurse

    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=(
            'Designates whether this user should be treated as active.'
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text=(
            'Designates whether the user can log ito this admin site and make changes.'
        ),
    )

    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    date_joined = models.DateTimeField(
        'date joined',
        default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'surname', 'id_no']

    def get_full_name(self):
        full_name = "{} {}".format(self.first_name, self.surname)
        return full_name.strip()

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
