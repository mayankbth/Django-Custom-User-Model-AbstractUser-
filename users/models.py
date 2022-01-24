from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils.translation import ugettext_lazy as _
# ugettext_lazy` was deprecated in v2.2 and no longer used in django v3+
# Django 4. ugettext_lazy has been removed in Django 4.0 86. use gettext_lazy instead
from django.utils.translation import gettext_lazy as _


from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
        1. Created a new class called CustomUser that subclasses AbstractUser
        2. Removed the username field
        3. Made the email field required and unique
        4. Set the USERNAME_FIELD -- which defines the unique identifier for the User model -- to email
        5. Specified that all objects for the class come from the CustomUserManager
    """
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
