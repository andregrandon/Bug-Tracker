from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission
from django.db import models

class UserProfile(AbstractUser):
    # Your other fields go here

    # Add a related_name to avoid clashes with auth.User
    groups = models.ManyToManyField(
        Permission,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to these groups.',
        related_name='user_profiles_groups',  # Add a unique related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='user_profiles_permissions',  # Add a unique related_name
    )
