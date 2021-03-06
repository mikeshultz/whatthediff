import uuid
from django.utils.translation import ugettext as _
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
    first_name = models.CharField("First Name", max_length=128)
    last_name = models.CharField("Last Name", max_length=128)
    email = models.EmailField("E-mail", unique=True, max_length=255, help_text = "E-mail address")
    is_admin = models.BooleanField("Is the user an admin?", default=False)

    USERNAME_FIELD = 'email'

    objects = WhatTheUserManager()

    class Meta:
        db_table = u'whatthediff_user'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

class InviteToken(models.Model):
    invitetoken_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    collection = models.ForeignKey('whatthecollection.Collection', null=True)
    can_write = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Invite Token')
        verbose_name_plural = _('Invite Tokens')

    def __unicode__(self):
        pass
