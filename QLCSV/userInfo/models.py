from django.db import models
from authentication.models import Account

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    image = models.ImageField(
        default='user_avatar.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user} Profile'
