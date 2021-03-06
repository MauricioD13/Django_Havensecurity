from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
