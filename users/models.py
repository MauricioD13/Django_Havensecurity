from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    """
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    Hay que instalar pillow (pip install pillow)           
    """

    def __str__(self):
        return self.user.username
