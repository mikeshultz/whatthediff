from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class WhatTheUserManager(BaseUserManager):
    """ Derp """
    def create_user(self, email, password, **kwargs):
        """ Creates and saves a User
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email), 
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        """ Creates a superuser
        """
        user = self.create_user(email, password, **kwargs)
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

class WhatTheUser(AbstractBaseUser):
    """ Custom user model so we can use email as pk """
    #username = models.CharField("E-mail", max_length=128, help_text = "E-mail address")
    email = models.EmailField("E-mail", unique=True, max_length=255, help_text = "E-mail address")

    USERNAME_FIELD = 'email'

    objects = WhatTheUserManager()

    class Meta:
        db_table = u'whatthediff_user'