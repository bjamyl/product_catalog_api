from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager




class UserAccountManager(BaseUserManager):
    # Creating a normal user
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must provide an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    # Creating an superuser
    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(username, email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user
    
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"
    
    def get_short_name(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.email
