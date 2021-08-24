from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.db.models.fields import CharField

class UserManager(BaseUserManager):

    def create_user(self,username,password=None,**extra_fields):  
        if not email:
            self.valueError('Users must have an email address')
        user= self.model(email=self.normalize_email(email),**extra_fields)          
        user.set_password(password)  
        user.save(using=self._db)

        return user
    def create_superuser(self, email, password):
         """Creates and saves a new super user"""
         user = self.create_user(email, password)
         user.is_staff = True
         user.is_superuser = True
         user.save(using=self._db)

         return user
         
class User(AbstractBaseUser,PermissionsMixin):

    email= models.EmailField(max_length=25,unique=True)
    name= CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserManager()
    USERNAME_FIELD='email'
# Create your models here.
