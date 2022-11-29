from django.db import models
from django.contrib.auth.models import User as UserDjango

# Create your models here.
class UserModel(UserDjango):
    class Meta:
        db_table = 'user'