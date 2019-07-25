from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
class UserManager(BaseUserManager):
    def create_user(self, email):
        if not email:
            raise ValueError("Users must have an email address")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user.save(using=self.db)
        return user

class User(AbstractBaseUser):
    email   = models.EmailField(max_length=255, unique=True)
