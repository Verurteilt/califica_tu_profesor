from django.db import models
from django.contrib.auth.models import AbstractBaseUser, _user_has_perm, PermissionsMixin, _user_has_module_perms
from django.utils.encoding import force_unicode as _
######################################

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    enrollment = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    rol = models.ForeignKey('Role', null=True)



    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'enrollment']


    def get_full_name(self):
        return _(self.first_name) + ' ' + _(self.last_name)

    def get_short_name(self):
        return _(self.first_name)

    def __unicode__(self):
        return _(self.first_name) + ' ' + _(self.last_name)

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        if self.is_active and self.is_superuser:
            return True
        return _user_has_module_perms(self, app_label)


    @property
    def is_staff(self):
        return self.is_admin

	@property
	def is_active(self):
		return self.is_active


class Role(models.Model):
	role = models.CharField(max_length=15, unique=True)
	key = models.CharField(max_length=10)