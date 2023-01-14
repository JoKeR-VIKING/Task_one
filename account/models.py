from django.db import models
from django.contrib.auth.models import User

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    address = models.TextField(max_length=400)
    is_doctor = models.BooleanField()

    def __str__(self):
        return self.user.username