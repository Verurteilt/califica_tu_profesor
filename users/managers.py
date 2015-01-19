from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self,enrollment, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        user = self.model(first_name=first_name, last_name=last_name, email=self.normalize_email(email), enrollment=enrollment)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, enrollment, first_name, last_name, email, password):
        user = self.create_user(enrollment, first_name, last_name, email, password )
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user