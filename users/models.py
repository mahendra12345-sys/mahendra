from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add your custom fields here (if any)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Add unique related_name
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Add unique related_name
        blank=True
    )
